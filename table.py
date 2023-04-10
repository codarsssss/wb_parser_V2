import mysql.connector


def save_to_mysql(data):
    connection = mysql.connector.connect(
        user='username',  # заменяем на актуальные данные
        password='password',
        host='localhost',
        database='database_name'
    )

    cursor = connection.cursor()

    sql = "INSERT INTO table_name (column1, column2, column3) VALUES (data[0], data[1], data[2])"  # заменяем на актуальные данные

    val = data  # передаем данные

    cursor.execute(sql, val)

    connection.commit()

    print(cursor.rowcount, "record inserted.")  # выводим сообщение о том, что данные были успешно сохранены

    cursor.close()

    connection.close()
