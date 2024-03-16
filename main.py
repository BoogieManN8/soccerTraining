from fastapi import FastAPI, File, UploadFile, Form, UploadFile, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import shutil, json, os
from datetime import date
from uuid import uuid4
from DatabaseManager import DatabaseManager
from models import *
from users import router as user_router
from collections import defaultdict



app = FastAPI()
db_manager = DatabaseManager()

app.mount("/videos", StaticFiles(directory="videos"), name="videos")
app.include_router(user_router, prefix="/api/v1", tags=["users"])



@app.get("/videos/{video_name}")
async def stream_video(video_name: str):
    video_path = os.path.join(VIDEOS_DIR, video_name)

    if not os.path.isfile(video_path):
        raise HTTPException(status_code=404, detail="Video not found")

    return FileResponse(path=video_path, media_type='video/mp4', filename=video_name)

@app.post("/upload-workout/")
async def upload_workout(
    workout_data: str = Form(...),
    exercises_data: str = Form(...),
    video: UploadFile = File(...)
):
    
    workout = json.loads(workout_data)
    exercises = json.loads(exercises_data)

    
    db_manager.connect()

    
    workout_id = db_manager.insert_workout(
        workout_date=workout['date'], 
        workout_type=workout['type'], 
        workout_level=workout['level']
    )

    
    for exercise in exercises:
        exercise_id = str(uuid4())
        video_filename = str(uuid4()) + os.path.splitext(video.filename)[-1]
        video_path = f"videos/{video_filename}"
        os.makedirs(os.path.dirname(video_path), exist_ok=True)
        with open(video_path, "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)
        
        
        db_manager.insert_exercise(
        exercise_id,
        exercise['name'],
        exercise['approach'],
        exercise['time'],
        exercise['repetition'],
        exercise['totalTime'],
        video_path,  
        workout_id,
        exercise.get('level', 0)  
    )


    db_manager.close()

    return {"message": "Workout and exercises uploaded successfully", "workoutId": workout_id}




@app.get("/workouts/", response_model=List[WorkoutDTO])
async def get_all_workouts():
    db_manager.connect()
    workouts = []
    with db_manager.connection.cursor() as cursor:
        # Adjusted query to include ORDER BY clause
        cursor.execute("SELECT id, date, type, level FROM workouts ORDER BY date ASC") 
        workout_records = cursor.fetchall()
        for workout_record in workout_records:
            cursor.execute("SELECT id, name, approach, time, repetition, totalTime, videoLink, level FROM exercises WHERE workoutId = %s", (workout_record['id'],))
            exercise_records = cursor.fetchall()
            
            exercises_by_level = defaultdict(list)
            for exercise_record in exercise_records:
                level_key = f"level{exercise_record['level']}"
                exercise_dto = ExerciseDTO(
                    id=exercise_record['id'],
                    name=exercise_record['name'],
                    approach=exercise_record['approach'],
                    time=exercise_record['time'],
                    repetition=exercise_record['repetition'],
                    totalTime=exercise_record['totalTime'],
                    videoLink=exercise_record['videoLink'],
                    level=exercise_record['level']  # Include the level attribute here
                )
                exercises_by_level[level_key].append(exercise_dto)
            
            workout_dto = WorkoutDTO(
                id=workout_record['id'],
                date=workout_record['date'],
                level=workout_record['level'],  
                type=workout_record['type'],
                exercises=dict(exercises_by_level)
            )
            workouts.append(workout_dto)
    db_manager.close()
    return workouts



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8008)
    
    
