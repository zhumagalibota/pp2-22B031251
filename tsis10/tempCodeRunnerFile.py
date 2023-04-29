connection = psycopg2.connect(host="localhost", port="5432", database="master", user="postgres", password="kbtu")

connection.autocommit = True
with connection.cursor() as cursor:
    cursor.execute("SELECT version();")
    print("Server version: {cursor.fetchone()}")