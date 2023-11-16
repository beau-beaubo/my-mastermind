"""Mastermind Game Project"""
import random


class Ball:
    """crate ball"""
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y
        self.position = []

    def random_number(self):
        """random number"""
        num = []
        for i in range(self.x):
            num.append(str(i+1))
        secret_num = random.sample(num, self.y)
        return secret_num

    def hint(self, guess_num, original_num):
        """create hint"""
        correct = []
        if guess_num == original_num:
            print("You win")
        else:
            for i in range(self.y):
                if guess_num[i] == original_num[i]:
                    correct.append('*')
                elif guess_num[i] in original_num:
                    correct.append('o')
        hint = ''
        for k in correct:
            hint += k
        print(hint)
        return hint

    def guess_number(self):
        """input msg"""
        list_guess = []
        guess = int(input("What is your guess:? "))
        guess = str(guess)
        for i in range(self.y):
            list_guess.append(guess[i])
        print('Your guess is', guess)
        return list_guess


color = int(input("Enter amount of color: "))
position = int(input("Enter amount of position: "))
while color > 8 or position > 10:
    print("invalid number")
    color = int(input("Enter amount of color (1-8) : "))
    position = int(input("Enter amount of position (1-10): "))
print("Playing Mastermind with", color, "colors and", position, "positions")
ball = Ball(color, position)
count = 0
_random = ball.random_number()
while True:
    _guess = ball.guess_number()
    check = ball.hint(_guess, _random)
    count += 1
    if _guess == _random:
        print("You solve it after", count, "round")
        break


