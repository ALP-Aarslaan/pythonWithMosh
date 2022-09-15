class Mammal:
    def make_sound(self):
        print(f" make sounds")


class Dog(Mammal):
    def bark(self):
        print("it barks")


class Cat(Mammal):
    def Meow(self):
        print("Its annoying")


dog1 = Dog()
dog1.bark()
dog1.make_sound()

cat = Cat()
cat.make_sound()
cat.Meow()