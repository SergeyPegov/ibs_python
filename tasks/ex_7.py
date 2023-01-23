class Animal:
    num_of_insts = 0

    def __init__(self):
        Animal.num_of_insts += 1

    def voice(self):
        pass

    def print_num():
        print("Instances created:", Animal.num_of_insts)

    print_num = staticmethod(print_num)

class Cat(Animal):
    def voice(self):
        print("Maay")


class Dog(Animal):
    def voice(self):
        print("Voof")


class Cow(Animal):
    def voice(self):
        print("Muuu")


Mursik = Cat()
Druzhok = Dog()
Marta = Cow()

Animal.print_num()

Mursik.voice()
Druzhok.voice()
Marta.voice()

