#!/usr/bin/env python3

import random
from math import floor
from difflib import SequenceMatcher
from game_logic import GameLogic

# This is the current version of WordLogic that needs to be adapted
class WordLogic(GameLogic):

    def word_selection(self):
        with open("words.txt") as f:
            word_list = f.read().splitlines()
        fixed_length_words = [word.upper() for word in word_list if len(word) is self.length]
        random.shuffle(fixed_length_words)
        sel_words = fixed_length_words[0:floor(self.num_words / 3)]
        reference_word = random.choice(sel_words)
        counter = 0
        while len(sel_words) < self.num_words:
            rand_word = fixed_length_words[floor(self.num_words / 3) + counter]
            if self.is_similar(reference_word, rand_word, 0.4):
                sel_words.append(rand_word)
            counter += 1
        return sel_words

    def is_similar(self, a, b, threshold):
        if SequenceMatcher(None, a, b).ratio() > threshold:
            return True
        else: return False

    def generate_feedback(self, guess):
        matching = 0
        for i in range(self.length):
            if guess[i] == self.password[i]: matching += 1
        self.attempts = self.attempts - 1
        return "%d/%d correct" % (matching, self.length)


if __name__ == "__main__":
    w = WordLogic(8, 4, 5)
    print(w.password)
    print(w.check(input()))