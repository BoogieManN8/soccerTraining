import pymysql
from datetime import datetime, timedelta

# Database configuration
database_config = {
    'host': "localhost",
    'user': "boogie",
    'password': "DontGazeSkugge",
    'database': "dimasapp"
}



workout_id_time_mapping = {
    12: "14:00:00",  
    2: "09:00:00",  
    5: "11:00:00",  
    8: "10:00:00",  
    14: "16:00:00",  
    11: "15:00:00",  
    4: "17:00:00",  
    10: "08:00:00",  
    13: "09:00:00",  
    3: "13:00:00",  
    1: "12:00:00",  
    7: "18:00:00",  
    6: "19:00:00",  
    9: "20:00:00",  
}

def update_workout_times(db_config, workout_id_time_mapping):
    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'],
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            for workout_id, time_str in workout_id_time_mapping.items():

                new_datetime = datetime.now() + timedelta(days=1)  
                new_datetime_str = new_datetime.strftime(f"%Y-%m-%d {time_str}")

                
                update_query = "UPDATE workouts SET date = %s WHERE id = %s"
                cursor.execute(update_query, (new_datetime_str, workout_id))

            
            connection.commit()
            print("Workout times updated successfully.")
    except Exception as e:
        print(f"Error updating workout times: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    update_workout_times(database_config, workout_id_time_mapping)
