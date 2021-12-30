try:
    class Customer:
        def __init__(self, surname, name, patronymic, phone):
            self.surname = surname
            self.name = name
            self.patronymic = patronymic
            self.phone = phone
    class Product:
        def __init__(self, price, desc, dim):
            self.price = price
            self.desc = desc
            self.dim = dim
    class Order:
        def __init__(self, guy: Customer, *args: Product):
            self.customer = guy
            self.products_ordered = args
        def str(self):
            return f'{self.guy}: \n {self.products_ordered}'
        def count(self) -> int:
            full_price = 0
            for i in self.products_ordered:
                full_price += i.price
            return full_price
    guy = Customer(input("Enter your surname: "), input("Enter your name: "), input("Enter your patronymic: "), int(input("Enter your phone number: ")))
    print("Surname: " + guy.surname, "Name: " + guy.name, "Patronymic: " + guy.patronymic, "Phone: " + str(guy.phone))
    obj1 = Product(int(input("Enter price: ")), input("Enter description: "), input("Enter dimensions: "))
    print("Price: " + str(obj1.price), "Description: " + obj1.desc, "Dimensions: " + obj1.dim)
    obj2 = Product(int(input("Enter price: ")), input("Enter description: "), input("Enter dimensions: "))
    print("Price: " + str(obj2.price), "Description: " + obj2.desc, "Dimensions: " + obj2.dim)
    obj3 = Product(int(input("Enter price: ")), input("Enter description: "), input("Enter dimensions: "))
    print("Price: " + str(obj3.price), "Description: " + obj3.desc, "Dimensions: " + obj3.dim)
    order = Order(guy, obj1, obj2, obj3)
    print(order.count())
except ValueError:
    print("Incorrect input")
