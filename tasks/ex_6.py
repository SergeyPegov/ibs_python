class Animal:
    def voice(self):
        pass

class Cat(Animal):
    def voice(self):
        print("Maay")
    pass

class Dog(Animal):
    def voice(self):
        print("Voof")
    pass

class Cow(Animal):
    def voice(self):
        print("Muuu")
    pass

Mursik = Cat()
Druzhok = Dog()
Marta = Cow()

Mursik.voice()
Druzhok.voice()
Marta.voice()