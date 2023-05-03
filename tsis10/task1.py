import psycopg2


try:
    connection = psycopg2.connect(host="localhost", 
    port="5432", database="master", 
    user="postgres", password="kbtu")

    connection.autocommit = True


    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         "SELECT version();"
    #     )
    #     print(cursor.fetchone())

    #creating the table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE phonebook(
    #             id serial PRIMARY KEY,
    #             name varchar(250) NOT NULL,
    #             phone varchar(250) NOT NULL);"""
    #     )
    # print("table created")

    # #inserting data
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO phonebook (name, phone) 
    #         VALUES ('C', '53538'),
    #         ('D','5436566');"""
    #     )
    # print("new data added")

    #insertiong data from csv file -------does not work
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """COPY phonebook(name, phone)
    #         FROM 'C:\\Users\\zhuma\\OneDrive\\Документы\\pp2\\tsis10\\persons (1).csv'
    #         DELIMITER ','
    #         CSV HEADER;""" 
    #     )
    # print("csv file added")

    #updating data
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """UPDATE phonebook SET phone = '1111111' WHERE name = 'A';"""
    #     )
    # print("updated")

    # #deleting data
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM phonebook WHERE name = 'B';"""
    #     )
    #     print("deleted")


    #querying sing fetchone() method
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT name, phone FROM phonebook ORDER BY id;"""
    #     )
    #     print("The number of rows:", cursor.rowcount)
    #     row = cursor.fetchone()
    #     while row is not None:
    #         print(row)
    #         row = cursor.fetchone()
    #     cursor.close()

    #querying using fetchall() method
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT name, phone FROM phonebook ORDER BY id;"""
    #     )
    #     rows = cursor.fetchall()
    #     print("the number of rows:", cursor.rowcount)
    #     for row in rows:
    #         print(row)
    #     cursor.close()


    #querying using fetchmany() method:
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT name, phone FROM phonebook 
    #         ORDER BY id;"""
    #     )
    #     rows = cursor.fetchmany(2)
    #     print(rows)
    #     cursor.close()


    #FILTERS
     # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT * FROM phonebook WHERE name = 'A';"""
    #     )
    #     print(cursor.fetchall())

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT name FROM phonebook GROUP BY name;"""
    #     )
    #     print(cursor.fetchall())

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT name FROM phonebook GROUP BY name HAVING count(name)>1;"""
    #     )
    #     print(cursor.fetchall())




except Exception as _ex:
    print("Error")
finally:
    connection.close()
    print("connection closed")