import json
import pymysql

# Database configuration
database_config = {
    'host': "localhost",
    'user': "boogie",
    'password': "DontGazeSkugge",
    'database': "dimasapp"
}

local_data_path = "local.json"

def update_video_links(local_data_path, db_config):
    # Load local data
    with open(local_data_path, 'r') as file:
        local_data = json.load(file)

    # Connect to the database
    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'],
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            for workout in local_data:
                # Assuming 'exercises_data' is the correct key based on your description
                for exercise in workout['exercises_data']:
                    # Update query
                    update_query = """
                        UPDATE exercises SET videoLink = %s WHERE name = %s
                    """
                    cursor.execute(update_query, (exercise['videoLink'], exercise['name']))

        # Commit changes
        connection.commit()
        print("Video links updated successfully.")
    except Exception as e:
        print(f"Error updating video links: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    update_video_links(local_data_path, database_config)
