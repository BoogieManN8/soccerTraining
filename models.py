from pydantic import BaseModel
from datetime import date
from typing import List, Dict,Optional
from datetime import datetime

class WorkoutHistoryBase(BaseModel):
    workout_date: datetime
    workout_details: str

class WorkoutHistoryCreate(BaseModel):
    workout_id: int
    workout_details: str
    workout_date: datetime  

class WorkoutHistoryDisplay(BaseModel):
    history_id: int
    user_id: str
    workout_id: int  
    workout_date: datetime
    workout_details: str


class ExerciseDTO(BaseModel):
    name: str
    approach: int
    time: int
    repetition: int
    totalTime: int
    videoLink: str

class WorkoutDTO(BaseModel):
    date: str
    type: str
    

class ExerciseDTO(BaseModel):
    id: str
    name: str
    approach: int
    time: int
    repetition: int
    totalTime: int
    videoLink: str
    level: int

class WorkoutDTO(BaseModel):
    history_id: Optional[int] = None
    id: int
    date: datetime
    level: int  
    type: str
    exercises: Dict[str, List[ExerciseDTO]]