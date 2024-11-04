print("refegerator")

class Human:

    def __init__(self, name="Anatolii"):
        self.name = name

class Auto:

    def __init__(self, shaslik):
        self.shaslik = shaslik
        self.perfarator = []

    def add_perfarator(self, *args):
        for perfarator in args:
            self.perfarator.append(perfarator)

    def print_perfarator_names(self):
        if self.perfarator !=[]:
            print(f"names of {self.shaslik} perfarator : ")
            for perfarator in self.perfarator:
                print(perfarator.name)
        else:
            print(f"There no perfarators in {self.shaslik}. refegerator...")

Anatolik = Human("Anatolik")
Ravhan = Human("Ravhan")
cat = Auto("Jigul")
cat.add_perfarator(Anatolik,Ravhan)
cat.print_perfarator_names()
