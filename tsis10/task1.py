import psycopg2

connection = psycopg2.connect(host="localhost", port="5432", database="master", user="postgres", password="kbtu")

connection.autocommit = True
with connection.cursor() as cursor:
    cursor.execute("SELECT version();")
    print("Server version: {cursor.fetchone()}")

# with connection.cursor() as cursor:
#     cursor.execute   (
#    """CREATE TABLE PHONEBOOK (
#     id SERIAL PRIMARY KEY,
#     phone_number VARCHAR(50) NOT NULL,
#     name VARCHAR(50) NOT NULL)"""
#     )
#     print("[INFO] Table created successfully")

# with connection.cursor() as cursor:
#     cursor.execute   (
#        """INSERT INTO PHONEBOOK (phone_number, name) VALUES ('8715451345', 'A');"""
#     )

with connection.cursor() as cursor:
    cursor.execute   (
       """SELECT phone_number FROM PHONEBOOK WHERE name = 'A';""" 
    )
    print(cursor.fetchone())