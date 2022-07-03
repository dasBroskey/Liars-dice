import random

class Player():

    def __init__(self, name, dice):
        self.name = name
        self.dice = dice
        self.cup = []
        self.guess = None

    def is_playing(self):
        if self.dice == 0:
            return False
        else:
            return True
        
    def remove_die(self):
        self.dice = self.dice - 1
        print(f"{self.name} lost a die!")
    
    def make_guess(self):
        die_guess = int(input("What number is your guess? "))
        amount_guess = int(input(f"How many {die_guess}'s are there? "))
        self.guess = (die_guess,amount_guess)

    def get_guess(self):
        return self.guess
    
    def mix(self):
        self.cup = []
        for _ in range(self.dice):
            self.cup.append(random.randint(1,6))
    
    def get_name(self):
        return self.name

    def get_cup(self,number):
        count = 0
        count += self.cup.count(number)
        count += self.cup.count(1)
        return count

    def get_dice(self):
        return self.cup

    def num_dice(self):
        return self.dice