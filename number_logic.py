#!/usr/bin/env python3

from game_logic import GameLogic
import random


class NumberLogic(GameLogic):

    def word_selection(self):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        res = []
        while len(res) < self.num_words:
            random.shuffle(numbers)
            rand_num = "".join(numbers[0:self.length])
            if not rand_num in res:
                res.append(rand_num)
        return res

    def generate_feedback(self, guess):
        matching = 0
        for number in guess:
            if number in self.password:
                matching += 1
        self.attempts = self.attempts - 1
        return "%d/%d correct" % (matching, self.length)

    def check(self, guess):
        if len(set(guess)) != len(guess): raise Warning("No duplicate numbers allowed")
        if len(guess) != self.length: raise Warning("Guess has the wrong length")
        return super().check(guess)


if __name__ == "__main__":
    n = NumberLogic(5, 4, 3)
    print(n.words)
    print(n.password)
    print(n.check(input()))