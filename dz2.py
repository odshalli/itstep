import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5

    def eat(self):
        if self.hunger < 8:
            self.hunger += 2
            self.energy += 1
            print(f"{self.name} поїла і тепер не сильно голодна.")
        else:
            print(f"{self.name} зараз не голодна.")
        self.status()

    def sleep(self):
        if self.energy < 8:
            self.energy += 3
            self.happiness += 1
            print(f"{self.name} поспала і тепер повна сил!")
        else:
            print(f"{self.name} не хоче спати ")
        self.status()

    def play(self):
        if self.energy > 2 and self.hunger > 1:
            self.happiness += 2
            self.energy -= 2
            self.hunger -= 1
            print(f"{self.name} пограла і тепер веселіша")
        else:
            print(f"{self.name} слишком уставша або голодна, щоб гратись.")
        self.status()

    def status(self):
        print(f"Стан {self.name}:")
        print(f"Голод: {self.hunger}/10, Єнегрія: {self.energy}/10, Щастя: {self.happiness}/10\n")

my_cat = Cat("Луна")

my_cat.status()
my_cat.eat()
my_cat.play()
my_cat.sleep()
