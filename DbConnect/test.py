# 1)Показать продукты
# 2)Создать продукт
# 3)Удалить продукт
# 1
# ...
import psycopg2


def change(sql):
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="kirito",
        password="passanya",
        dbname="crm"
    )
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


def select(sql):
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="kirito",
        password="passanya",
        dbname="crm"
    )
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return data
