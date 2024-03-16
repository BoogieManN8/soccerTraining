import pymysql.cursors
import json
from datetime import datetime
from pymysql.err import IntegrityError
from typing import List, Dict
import uuid

class ExerciseDTO:
    def __init__(self, id, name, approach, time, repetition, totalTime, videoLink, level):
        self.id = id
        self.name = name
        self.approach = approach
        self.time = time
        self.repetition = repetition
        self.totalTime = totalTime
        self.videoLink = videoLink
        self.level = level

class WorkoutDTO:
    def __init__(self, id, date, level, type, exercises):
        self.id = id
        self.date = date
        self.level = level
        self.type = type
        self.exercises = exercises
        
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


def main():
    current_datetime = datetime.now()
    user_id = "58f7fe6a-a4ba-44f8-9d75-0144fe47b5db"
    available_workout_ids = get_available_workout_ids(user_id)
    filtered = filetr_workouts(available_workout_ids, available_workout_ids)
    print(load_workouts_from_json())



def upload_data_to_database(data: list):
    connection = pymysql.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            for workout in data:
                workout_data = workout['workout_data']
                exercises_data = workout['exercises_data']

                # Insert into workouts table
                workout_insert_query = """
                INSERT INTO workouts (date, type, level)
                VALUES (%s, %s, %s)
                """
                cursor.execute(workout_insert_query, (workout_data['date'], workout_data['type'], workout_data['level']))
                workout_id = connection.insert_id()  # Retrieve the last inserted 'id' of workout

                # Insert into exercises table
                for exercise in exercises_data:
                    exercise_id = str(uuid.uuid4())  # Generate a UUID for each exercise
                    exercise_insert_query = """
                    INSERT INTO exercises (id, name, approach, time, repetition, totalTime, videoLink, workoutId, level)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(exercise_insert_query, (exercise_id, exercise['name'], exercise['approach'], exercise['time'], 
                                                            exercise['repetition'], exercise['totalTime'], 
                                                            exercise['videoLink'], workout_id, exercise['level']))

            connection.commit()
    except Exception as e:
        print(f"Failed to insert data: {e}")
        connection.rollback()  # Roll back in case of error
    finally:
        connection.close()
if __name__ == "__main__":
    data = load_workouts_from_json()
    upload_data_to_database(data)