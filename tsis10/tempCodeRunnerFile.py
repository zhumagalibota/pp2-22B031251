with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT name, phone FROM phonebook ORDER BY id;"""
    #     )
    #     print("The number of rows:", cursor.rowcount)
    #     row = cursor.fetchone()
    #     while row is not None:
    #         print(row)
    #         row = cursor.fetchone()
    #     corsor.close()