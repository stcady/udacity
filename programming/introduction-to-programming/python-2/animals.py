class Dog:

    scientific_name = "Canis lupus familiaris"

    def speak(self):
        print("Woof!")

    def eat(self, food):
        if food == "biscuit":
            print("Yummy!")
        else:
            print("That's not food!")

    def learn_name(self, name):
        self.name = name

    def hear(self, words):
        if self.name in words:
            self.speak()