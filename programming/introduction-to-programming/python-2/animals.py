class Dog:

    scientific_name = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name
        self.woofs = 0

    def speak(self):
        print("Woof!")

    def eat(self, food):
        if food == "biscuit":
            print("Yummy!")
        else:
            print("That's not food!")

    def hear(self, words):
        if self.name in words:
            self.speak()

    def woofs(self):
        count += 1
        for i in range(count):
            self.speak()

    def do_trick():
        pass

class Chihuahua(Dog):
    
    origina = 'Mexico'
    
    def speak(self):
        print("Yip!")

    def do_trick(self):
        pass

class TrainedChihuahua(Dog):

    def do_trick(self):
        print("Chihuahua does a trick!")