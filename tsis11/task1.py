import psycopg2


try:
    connection = psycopg2.connect(host="localhost", 
    port="5432", database="master", 
    user="postgres", password="kbtu")

    connection.autocommit = True

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

    # with connection.cursor() as cursor:
    #     cursor.execute( """INSERT INTO phonebook (name, phone) 
    #         VALUES ('A', '53538'),
    #         ('A','5436566');""")
    # print("updated")


    #returns records based on a pattern
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT * FROM phonebook WHERE name = 'A';"""
    #     )
    #     print(cursor.fetchall())
    

    # 4 limit and offset
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT * FROM phonebook ORDER BY name LIMIT 2 OFFSET 3;"""
    #     )
    #     print(cursor.fetchall())
    

    #1
    # engine = connection.cursor()

    # engine.callproc('records', [pattern, 'A'])
    # print(cursor.fetchall())

    #4
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE FUNCTION pagination(num1 integer, num2 integer) RETURNS TABLE(name varchar, phone varchar) AS 
    #    $$
    #    BEGIN
    #    SELECT * FROM phonebook ORDER BY name LIMIT num1 OFFSET num2;
    #    END;
    #    $$
    #    LANGUAGE plpgsql;"""
    #     )

    # cursor.callproc('pagination', [2, 3])
    # print(cursor.fetchall())

    #2
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE PROCEDURE upd(pattern varchar, phone varchar)
    #         LANGUAGE plpgsql
    #         AS 
    #         $$
    #         BEGIN
    #           UPDATE phonebook SET phone = phone WHERE name = pattern;
    #         END;
    #         $$;"""
    #     )
    #     cursor.callproc('upd', ['C', '55555'])
    #     print(cursor.fetchall())

    #3
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO phonebook(name, phone)
            VALUES
            ('B', '456664'),
            ('F', '55689');"""
        )
        print(cursor.fetchall())



#     #5
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """CREATE PROCEDURE del(pattern varchar)
# LANGUAGE plpgsql
# AS 
# $$
# BEGIN
#   DELETE FROM phonebook WHERE name = pattern;
# END;
# $$;"""
#         )
#         cursor.callproc('del', ('D'))
#         print(cursor.fetchall())


except Exception as _ex:
    print("Error")
finally:
    connection.close()
    print("connection closed")