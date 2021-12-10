#!/usr/bin/env python3

from abc import ABC, abstractmethod
import random

class GameLogic(ABC):
    """Internal game logic"""

    def __init__(self, num_words, length, attempts):
        """Set up a new game with the provided parameters"""
        self.num_words = num_words
        self.length = length
        self.attempts = attempts
        self.words = self.word_selection()
        self.password = random.choice(self.words)

    def check(self, guess):
        """Check a guess and give feedback"""
        if len(guess) != self.length:
            return False, ["Wrong length"]
        if guess == self.password:
            return True, ["Access granted!"]
        else:
            return False, [
                self.generate_feedback(guess),
                "Access denied!"
            ]

    @abstractmethod
    def word_selection(self):
        pass

    @abstractmethod
    def generate_feedback(self, guess):
        pass