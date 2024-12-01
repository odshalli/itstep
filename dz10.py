class МоваПрограмування:
    def __init__(self, name):
        self.name = name

    def вивести_привітання(self):
        print(f"Привіт! Я - мова програмування {self.name}.")

class Python(МоваПрограмування):
    def __init__(self):
        super().__init__("Python")

    def вивести_привітання(self):
        super().вивести_привітання()
        print("Я відомий своєю простотою та широким використанням у науці про дані.")

class JavaScript(МоваПрограмування):
    def __init__(self):
        super().__init__("JavaScript")

    def вивести_привітання(self):
        super().вивести_привітання()
        print("Я чудовий для веб-розробки та створення інтерактивних веб-сторінок.")

class Cpp(МоваПрограмування):
    def __init__(self):
        super().__init__("C++")

    def вивести_привітання(self):
        super().вивести_привітання()
        print("Я використовуюсь для високопродуктивного програмування та розробки ігор.")

python = Python()
javascript = JavaScript()
cpp = Cpp()

python.вивести_привітання()
javascript.вивести_привітання()
cpp.вивести_привітання()
