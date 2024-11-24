class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, stock={self.stock})"


class Cart:
    def __init__(self):

        self.items = {}

    def add_product(self, product, quantity):
        if product.stock < quantity:
            print(f"Недостатньо товару {product.name} на складі (доступно: {product.stock}).")
            return
        if product.name in self.items:
            self.items[product.name]["quantity"] += quantity
        else:
            self.items[product.name] = {"product": product, "quantity": quantity}
        product.stock -= quantity
        print(f"{quantity} одиниць товару {product.name} додано до кошика.")

    def remove_product(self, product_name, quantity):
        if product_name not in self.items:
            print(f"Товар {product_name} не знайдено в кошику.")
            return
        if self.items[product_name]["quantity"] < quantity:
            print(f"В кошику немає достатньої кількості {product_name} (є {self.items[product_name]['quantity']}).")
            return
        self.items[product_name]["quantity"] -= quantity
        self.items[product_name]["product"].stock += quantity
        if self.items[product_name]["quantity"] == 0:
            del self.items[product_name]
        print(f"{quantity} одиниць товару {product_name} видалено з кошика.")

    def calculate_total(self):

        total = sum(item["product"].price * item["quantity"] for item in self.items.values())
        return total

    def list_cart_items(self):

        if not self.items:
            print("Кошик порожній.")
        else:
            print("Товари у кошику:")
            for item in self.items.values():
                product = item["product"]
                quantity = item["quantity"]
                print(f"  - {product.name}: {quantity} шт. x {product.price} = {quantity * product.price}")

if __name__ == "__main__":
    product1 = Product("Хліб", 30, 50)
    product2 = Product("Молоко", 25, 30)
    product3 = Product("Сир", 80, 20)

    cart = Cart()

    cart.add_product(product1, 2)
    cart.add_product(product2, 3)
    cart.add_product(product3, 1)

    cart.list_cart_items()

    print(f"Загальна вартість: {cart.calculate_total()} грн")

    cart.remove_product("Молоко", 2)

    cart.list_cart_items()
    print(f"Загальна вартість: {cart.calculate_total()} грн")
