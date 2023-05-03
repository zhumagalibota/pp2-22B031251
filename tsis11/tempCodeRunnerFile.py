with connection.cursor() as cursor:
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