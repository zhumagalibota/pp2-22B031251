import psycopg2

connection = psycopg2.connect(host="localhost", 
    port="5432", database="database", 
    user="postgres", password="kbtu")
try:

    connection.autocommit = True
  

    #creating the table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
                id serial PRIMARY KEY,
                user varchar(250) NOT NULL,
                score varchar(250) NOT NULL 
            );"""
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (user, score) 
            VALUES ('C', '53538'),
            ('D','5436566');"""
        )
   

except Exception as _ex:
    print("Error")
finally:
    connection.close()
    print("connection closed")