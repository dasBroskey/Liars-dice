import random

class Die():

    def __init__(self):
        self.number = None

    def get_number(self):
        return self.number

    def roll(self):
        self.number = random.randint(1,6)