from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import pymysql.cursors
import uuid
from models import *
from collections import defaultdict
import json

router = APIRouter()




DB_CONFIG = {
    'host': "localhost",
    'user': "boogie",
    'password': "DontGazeSkugge",
    'database': "dimasapp"
}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

def load_workouts_from_json() -> List[Dict]:
    with open('local.json') as f:
        return json.load(f)
    
def get_available_workout_ids(user_id: str) -> List[int]:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            query = """
            SELECT DISTINCT w.id, w.date, w.type, w.level FROM workouts w
            LEFT JOIN workout_history h ON w.id = h.workout_id AND h.user_id = %s
            WHERE w.date > %s OR h.workout_id IS NULL
            ORDER BY w.date ASC
            """
            now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(query, (user_id, now_str))
            result = cursor.fetchall()
            
            return [row[0] for row in result]



def filetr_workouts(ids: [int], available: [int]):
    data = load_workouts_from_json()
    return [data[ctr] for ctr, id in enumerate(available) if id in ids]

class UserBase(BaseModel):
    id: str
    token: str
    level: int
    goal: Optional[int] = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    token: str
    level: int
    goal: Optional[int] = None
    
    

class PointsUpdateRequest(BaseModel):
    points: int


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
        sql = "INSERT INTO users (id, token, level, goal) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (user.id, user.token, user.level, user.goal))
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
        sql = "UPDATE users SET token = %s, level = %s, goal = %s WHERE id = %s"
        cursor.execute(sql, (user.token, user.level, user.goal, user_id))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        db.commit()
    return {**user.dict(), "id": user_id}


@router.patch("/users/{user_id}/points", response_model=dict)
def update_user_points(user_id: str, points_update: PointsUpdateRequest, db=Depends(get_db)):
    with db.cursor() as cursor:

        sql = "UPDATE users SET points = %s WHERE id = %s"
        cursor.execute(sql, (points_update.points, user_id))
        affected_rows = cursor.rowcount
        db.commit()
        
    if affected_rows:

        return {"message": "success"}
    else:

        return {"message": "failure"}



def get_db():
    return pymysql.connect(
        host="localhost",
        user="boogie",
        password="DontGazeSkugge",
        database="dimasapp",
        cursorclass=pymysql.cursors.DictCursor
    )



@router.get("/users/{user_id}/available_workouts/", response_model=List[WorkoutDTO])
def get_available_workouts(user_id: str, db=Depends(get_db)):

    current_datetime = datetime.now()
    available_workout_ids = get_available_workout_ids(user_id)
    filtered = filetr_workouts(available_workout_ids, available_workout_ids)
    # workouts_dto = transform_to_workout_dto(filtered_workouts)
    
    return filtered

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