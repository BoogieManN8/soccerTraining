import pymysql
from datetime import datetime, timedelta
from fastapi import Depends

# Database configuration
database_config = {
    'host': "localhost",
    'user': "boogie",
    'password': "DontGazeSkugge",
    'database': "dimasapp"
}



workout_id_time_mapping = {
    34: "09:00:00",
    35: "10:00:00",
    36: "11:00:00",
    37: "14:00:00",
    38: "15:00:00",
    39: "16:00:00",
    40: "17:00:00",
    41: "08:00:00",
    42: "09:00:00",
    43: "12:00:00",
    44: "13:00:00",
    45: "18:00:00",
    46: "19:00:00",
    47: "20:00:00",
}

# def update_workout_times(db_config, workout_id_time_mapping):
#     connection = pymysql.connect(
#         host=db_config['host'],
#         user=db_config['user'],
#         password=db_config['password'],
#         database=db_config['database'],
#         cursorclass=pymysql.cursors.DictCursor
#     )

#     workout_ids = list(workout_id_time_mapping.keys())
#     half_point = len(workout_ids) // 2  

#     try:
#         with connection.cursor() as cursor:
#             for i, workout_id in enumerate(workout_ids):
                
#                 days_to_add = 1 if i < half_point else 2
#                 new_datetime = datetime.now() + timedelta(days=days_to_add)
#                 time_str = workout_id_time_mapping[workout_id]
#                 new_datetime_str = new_datetime.strftime(f"%Y-%m-%d {time_str}")

#                 update_query = "UPDATE workouts SET date = %s WHERE id = %s"
#                 cursor.execute(update_query, (new_datetime_str, workout_id))
#                 print(f"update query {new_datetime}")
#             connection.commit()
#             print("Workout times updated successfully.")
#     except Exception as e:
#         print(f"Error updating workout times: {e}")
#     finally:
#         connection.close()

def get_db():
    return pymysql.connect(
        host="localhost",
        user="boogie",
        password="DontGazeSkugge",
        database="dimasapp",
        cursorclass=pymysql.cursors.DictCursor
    )
    
def update_workout_times(db_config, workout_id_time_mapping):
    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'],
        cursorclass=pymysql.cursors.DictCursor
    )

    workout_ids = list(workout_id_time_mapping.keys())
    half_point = len(workout_ids) // 2  

    try:
        with connection.cursor() as cursor:
            for i, workout_id in enumerate(workout_ids):
                days_to_add = 1 if i < half_point else 2
                new_datetime = datetime.now() + timedelta(days=days_to_add)
                time_str = workout_id_time_mapping[workout_id]
                new_datetime_str = new_datetime.strftime(f"%Y-%m-%d {time_str}")
                update_query = "UPDATE workouts SET date = %s WHERE id = %s"
                cursor.execute(update_query, (new_datetime_str, workout_id))
                print(f"Updated workout ID {workout_id} to new datetime: {new_datetime_str}")
            connection.commit()
            print("Workout times updated successfully.")
    except Exception as e:
        print(f"Error updating workout times: {e}")
    finally:
        connection.close()

def get_all():
    q = """
    select date from workouts;
    """
    with get_db().cursor() as cursor:
        cursor.execute(q)
        
        res = cursor.fetchall()
        for item in res:
            print(f"item - {item}" , end="\n\n")
            
    

if __name__ == "__main__":
    update_workout_times(database_config, workout_id_time_mapping)
    # get_all()