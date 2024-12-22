import psycopg2
import dj_database_url
from datetime import datetime

# Your Render Database URL (replace this with your actual URL)
DATABASE_URL = "postgresql://bookyourshow_user:OdnZ2aYigGIP9EmCXmxO5LMVWExm7UMs@dpg-ctjh4152ng1s73bjmd80-a.oregon-postgres.render.com/bookyourshow"

# Parse the URL to extract connection parameters
db_params = dj_database_url.parse(DATABASE_URL)

try:
    # Establish the connection using parsed parameters
    conn = psycopg2.connect(
        dbname=db_params['NAME'],
        user=db_params['USER'],
        password=db_params['PASSWORD'],
        host=db_params['HOST'],
        port=db_params['PORT']
    )

    # Create cursor object
    cur = conn.cursor()

    # Sample SQL queries to insert data
    queries = [
     
    
    # INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
    # VALUES
    #     (2, 'pbkdf2_sha256$600000$NNzKBxaHZP8M1uwh44xTfV$GSBiJOBo/T6qgitAtcd7qCF8S0cJ8wdbnxfTwBDdwTM=', '2024-12-21 19:29:52+00', FALSE, 'Sample', '', '', 'chintalasasank2003@gmail.com', FALSE, TRUE, '2024-12-21 19:29:50+00');
    # ,
    # """
#     INSERT INTO movies_seat (id, theater_id, seat_number, is_booked)
# VALUES
#     (6, 2, 'A1', FALSE),
#     (7, 2, 'A2', FALSE),
#     (8, 2, 'A3', FALSE),
#     (9, 2, 'B1', FALSE),
#     (10,2, 'B2', FALSE),

#     (11, 3, 'A1', FALSE),
#     (12, 3, 'A2', FALSE),
#     (13, 3, 'A3', FALSE),
#     (14, 3, 'B1', FALSE),
#     (15, 3, 'B2', FALSE),
#     (16, 4, 'A1', FALSE),
#     (17, 4, 'A2', FALSE),
#     (18, 4, 'A3', FALSE),
#     (19, 4, 'B1', FALSE),
#     (20, 4, 'B2', FALSE);
        
#     """


"""UPDATE movies_seat
SET is_booked = FALSE
WHERE is_booked = TRUE;"""

   
]

    

    # Execute the queries
    for query in queries:
        cur.execute(query)
    
    # Commit the transaction
    conn.commit()

    print("Data inserted successfully")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()
