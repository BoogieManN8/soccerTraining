from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import pymysql.cursors
import uuid
from models import *
from collections import defaultdict

router = APIRouter()

class UserBase(BaseModel):
    id: str
    token: str
    level: int

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    token: str
    level: int


def get_db():
    connection = pymysql.connect(host='localhost',
                                 user='boogie',
                                 password='DontGazeSkugge',
                                 database='dimasapp',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        yield connection
    finally:
        connection.close()

@router.post("/users/", response_model=UserBase)
def create_user(user: UserCreate, db=Depends(get_db)):
    with db.cursor() as cursor:
        sql = "INSERT INTO users (id, token, level) VALUES (%s, %s, %s)"
        cursor.execute(sql, (str(user.id), user.token, user.level))
        db.commit()
    return user

@router.get("/users/", response_model=List[UserBase])
def read_users(skip: int = 0, limit: int = 10, db=Depends(get_db)):
    with db.cursor() as cursor:
        sql = "SELECT id, token, level FROM users LIMIT %s OFFSET %s"
        cursor.execute(sql, (limit, skip))
        result = cursor.fetchall()
    return result

@router.get("/users/{user_id}", response_model=UserBase)
def read_user(user_id: str, db=Depends(get_db)):
    with db.cursor() as cursor:
        sql = "SELECT id, token, level FROM users WHERE id = %s"
        cursor.execute(sql, (user_id,))
        result = cursor.fetchone()
        if result is None:
            raise HTTPException(status_code=404, detail="User not found")
    return result

@router.put("/users/{user_id}", response_model=UserBase)
def update_user(user_id: str, user: UserUpdate, db=Depends(get_db)):
    with db.cursor() as cursor:
        sql = "UPDATE users SET token = %s, level = %s WHERE id = %s"
        cursor.execute(sql, (user.token, user.level, user_id))
        db.commit()
    return {**user.dict(), "id": user_id}


@router.get("/users/{user_id}/available_workouts/", response_model=List[WorkoutDTO])
def get_available_workouts(user_id: str, db=Depends(get_db)):
    with db.cursor() as cursor:
        # Fetch IDs of workouts the user has completed
        cursor.execute("SELECT workout_id FROM workout_history WHERE user_id = %s", (user_id,))
        completed_workouts = cursor.fetchall()
        completed_ids = [workout['workout_id'] for workout in completed_workouts]

        # Fetch available workouts not completed by the user
        query = """
        SELECT id, date, type, level FROM workouts
        WHERE id NOT IN (%s)
        """ % ', '.join(['%s'] * len(completed_ids)) if completed_ids else "SELECT id, date, type, level FROM workouts"

        cursor.execute(query, completed_ids)
        available_workouts = cursor.fetchall()

        workouts = []
        for workout in available_workouts:
            cursor.execute("SELECT * FROM exercises WHERE workoutId = %s", (workout['id'],))
            exercises = cursor.fetchall()

            exercises_by_level = defaultdict(list)
            for exercise in exercises:
                level_key = f"level{exercise['level']}"
                exercises_by_level[level_key].append(ExerciseDTO(
                    id=exercise['id'],
                    name=exercise['name'],
                    approach=exercise['approach'],
                    time=exercise['time'],
                    repetition=exercise['repetition'],
                    totalTime=exercise['totalTime'],
                    videoLink=exercise['videoLink'],
                    level=exercise['level']
                ))
            
            workouts.append(WorkoutDTO(
                id=workout['id'],
                date=workout['date'],
                level=workout['level'],
                type=workout['type'],
                exercises=dict(exercises_by_level)
            ))

    return workouts


@router.delete("/users/{user_id}")
def delete_user(user_id: str, db=Depends(get_db)):
    with db.cursor() as cursor:
        sql = "DELETE FROM users WHERE id = %s"
        cursor.execute(sql, (user_id,))
        db.commit()
    return {"detail": "User deleted successfully"}


@router.post("/users/{user_id}/workout_history/", response_model=WorkoutHistoryDisplay)
def add_workout_history(user_id: str, workout_history: WorkoutHistoryCreate, db=Depends(get_db)):
    with db.cursor() as cursor:
        # Ensure the user exists
        cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
        if cursor.fetchone() is None:
            raise HTTPException(status_code=404, detail="User not found")

        # Insert workout history with workout_id
        sql = "INSERT INTO workout_history (user_id, workout_id, completion_date, workout_details) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (user_id, workout_history.workout_id, workout_history.workout_date, workout_history.workout_details))
        db.commit()
        history_id = cursor.lastrowid

        return {
            "history_id": history_id,
            "user_id": user_id,
            "workout_id": workout_history.workout_id,
            "workout_date": workout_history.workout_date,
            "workout_details": workout_history.workout_details
        }


@router.get("/users/{user_id}/workout_history/", response_model=List[WorkoutDTO])
def get_workout_history(user_id: str, db=Depends(get_db)):
    workouts = []
    with db.cursor() as cursor:

        cursor.execute("SELECT history_id, workout_id, completion_date, workout_details FROM workout_history WHERE user_id = %s", (user_id,))
        history_records = cursor.fetchall()

        for record in history_records:
            workout_id = record['workout_id']
            history_id = record['history_id']  

            # Fetch the workout details
            cursor.execute("SELECT id, date, type, level FROM workouts WHERE id = %s", (workout_id,))
            workout_record = cursor.fetchone()
            if not workout_record:
                continue

            # Fetch exercises associated with the workout
            cursor.execute("SELECT * FROM exercises WHERE workoutId = %s", (workout_id,))
            exercise_records = cursor.fetchall()

            exercises_by_level = defaultdict(list)
            for exercise_record in exercise_records:
                level_key = f"level{exercise_record['level']}"
                exercises_by_level[level_key].append(ExerciseDTO(
                    id=exercise_record['id'],
                    name=exercise_record['name'],
                    approach=exercise_record['approach'],
                    time=exercise_record['time'],
                    repetition=exercise_record['repetition'],
                    totalTime=exercise_record['totalTime'],
                    videoLink=exercise_record['videoLink'],
                    level=exercise_record['level']
                ))

            workout_dto = WorkoutDTO(
                history_id=history_id,  
                id=workout_record['id'],
                date=workout_record['date'],
                level=workout_record['level'],
                type=workout_record['type'],
                exercises=dict(exercises_by_level)
            )
            workouts.append(workout_dto)

    return workouts