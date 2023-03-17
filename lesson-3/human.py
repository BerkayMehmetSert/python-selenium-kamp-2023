class Human:
    # name = "James"
    def __init__(self, name):  # Constructor method
        self.name = name
        print("Human instance is created")

    # def __str__(self) -> str:  # String representation of the object
    #     return f"Human(name={self.name})"

    def __str__(self):  # String representation of the object
        return f"Human(name={self.name})"

    def talk(self, sentence):
        print(f"{self.name}: {sentence}")
        # self.walk()

    def walk(self):
        print(f"{self.name} is walking")
