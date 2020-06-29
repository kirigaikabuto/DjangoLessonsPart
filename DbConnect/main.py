from test import *


def show_products():
    sql = "select * from products"
    products = select(sql)
    for i in products:
        print(i)
    main()


def add_product():
    name = input("name:")
    price = int(input("price:"))
    sql=f"insert into products (name,price) values ('{name}','{price}')"
    change(sql)
    print("товар успешно добавлен")
    main()


def update_product():
    sql = "select * from products"
    products = select(sql)
    for i in products:
        print(i)
    print("выбери продукт по id")
    id = int(input("id:"))
    fields = ["name", "price"]
    properties = input("выбери свойство которое хочешь поменять:")
    if properties not in fields:
        print("нет такого поля")
        update_product()
    value = input("напиши новое значение этого поля:")
    sql = f"update products set {properties}='{value}' where id='{id}'"
    change(sql)
    print("продукт был обновлен")
    main()


def main():
    print("[1]Вывести все продукты")
    print("[2]Добавить новый продукт")
    print("[3]Обновить данные о продукте")
    print("[4]Удалить данные о продукте")
    num = int(input())
    if num == 1:
        show_products()
    elif num == 2:
        add_product()
    elif num == 3:
        update_product()
    elif num == 4:
        pass


main()
