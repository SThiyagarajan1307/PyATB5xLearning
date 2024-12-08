class Dog:
    # A
    name = None
    breed = None
    height = None
    weight = None

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass


# Object Ref
chow = Dog()
# Dog() - Object
# chow -> Object Ref.
chow.bark()
chow.talk()

#Create multiple Object for same class
mow = Dog()
bow = Dog()
rancho = Dog()
