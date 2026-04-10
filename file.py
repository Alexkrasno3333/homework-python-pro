import json
import random

def load():
    with open('database.json', 'r') as f:
        print(json.load(f))
        return


class Product:
    def __init__(self,name, category, price, stock ):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.product_id = random.randint(1,100000)

    def promotion(self):
        self.price = self.price * 0.9

    def warehouse_product (self):
        if self.stock > 0:
            self.stock -= 1
        else:
            print("Товара нет на складе")

    def __str__(self):
        return f"{self.name} | {self.category} | {self.price} грн | на складе: {self.stock}"


class Customer:
    def __init__(self, name, email, amount):
        self.name = name
        self.email = email
        self.amount = amount
        self.order_list = []
        self.customer_id = random.randint(1,100000)

    def add_order(self, new_order):
        self.order_list.append(new_order)

    def user_amount(self, order):
        if self.amount >= order.calculate_total():
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} | {self.email} | заказов: {len(self.order_list)} | баланс: {self.amount}"


class Order:
    def __init__(self, customer_id):
        self.product_list = []
        self.total_price = 0
        self.customer_id = customer_id
        self.order_id = random.randint(1, 100000)

    def add_product(self, product):
        self.product_list.append(product)

    def calculate_total(self):
        total = 0
        for product in self.product_list:
            total += product.price
        self.total_price = total
        return total

    def save(self):
        new_order = {
        "order_id": self.order_id,
        "customer_id": self.customer_id,
        "total_price": self.total_price,
        "product_ids": [product.product_id for product in self.product_list]
    }
        try:
            with open('database.json', 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(new_order)

        with open('database.json', 'w') as f:
            json.dump(data, f)

def main():
    load()

    p1 = Product("Lego City", "конструктор", 1200, 15)
    p2 = Product("Медведь", "мягкая-игрушка", 400, 10)
    p3 = Product("Машина", "твердая-игрушка", 800, 5)
    products = [p1, p2, p3]

    bob = Customer("Bob", "wer@1235.gameil.cvom",10000)
    print("Добро пожаловать в магазин")

    user = input("\nХочешь скидку 10 процентов: yes or no: ").lower()
    if user == 'yes':
        for product in products:
            product.promotion()

    while True:
        print(f"\nТвой аккаунт: {bob}")

        print("\nТовары:")
        for product in products:
            print(product)

        print("\n1 - Lego City")
        print("2 - Медведь")
        print("3 - Машина")

        user = input("Выберите товар: ")

        order1 = Order(bob.customer_id)

        if user == '1':
            selected_product = products[0]
        elif user == '2':
            selected_product = products[1]
        elif user == '3':
            selected_product = products[2]
        else:
            print("Неверный выбор")
            continue

        order1.add_product(selected_product)
        total = order1.calculate_total()

        print("Сумма заказа:", total)

        if bob.user_amount(order1):
            bob.amount -= total
            selected_product.warehouse_product()
            bob.add_order(order1)
            order1.save()
            print("Покупка успешна")

        else:
            print("Не хватает денег")

        again = input("Купить ещё? yes/no: ").lower()
        if again != 'yes':
            break

    print("\nОстаток товаров:")
    for product in products:
        print(product)

    print(f"\nТвой аккаунт: {bob}")


main()


















