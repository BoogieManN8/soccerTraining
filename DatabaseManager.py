import pymysql
from uuid import uuid4
from fastapi import Depends



class DatabaseManager:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'boogie'
        self.password = 'DontGazeSkugge'
        self.database = 'dimasapp'
        self.connection = None
    
    def connect(self):
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.DictCursor
        )
    
    def close(self):
        if self.connection:
            self.connection.close()

    def insert_workout(self, workout_date, workout_type, workout_level):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO workouts (date, type, level) VALUES (%s, %s, %s)"
            cursor.execute(sql, (workout_date, workout_type, workout_level))
            self.connection.commit()
            return cursor.lastrowid

    def insert_exercise(self, id, name, approach, time, repetition, totalTime, videoLink, workoutId, level):
        with self.connection.cursor() as cursor:
            sql = """INSERT INTO exercises (id, name, approach, time, repetition, totalTime, videoLink, workoutId, level) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (
                id, name, approach, time, repetition, totalTime, videoLink, workoutId, level
            ))
            self.connection.commit()
            
            
    def fetch_all_workouts(self):
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM workouts")
            workouts = cursor.fetchall()
        self.close()
        return workouts

    def fetch_exercises_for_workout(self, workout_id):
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM exercises WHERE workoutId = %s", (workout_id,))
            exercises = cursor.fetchall()
        self.close()
        return exercises
    
    def delete_exercise(self, exercise_id):
        self.connect()
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM exercises WHERE id = %s"
            cursor.execute(sql, (exercise_id,))
            self.connection.commit()
        self.close()
