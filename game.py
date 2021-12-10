#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
from word_logic import WordLogic
from number_logic import NumberLogic



class GameRunner:
    """Interactive game front-end"""

    def __init__(self, logic):
        """Interact with the given game logic"""
        self.logic = logic
        self.rows = 17
        self.columns = 2
        self.colwidth = 12
        self.code_snippet = self.generate_code_lines()
        self.hex_codes = self.generate_hex_codes()

    def generate_hex_codes(self):
        __pos_values = "0123456789ABCDEF"
        return ["0x" + "".join(random.choices(__pos_values, k=4)) for time in range(self.columns * self.rows)]

    def generate_code_lines(self):
        padding_chars = "<>[]{}()'|\"!@#$%^&*-_+=.;:?,/"
        len_snippet = self.rows * self.columns * self.colwidth
        len_words = self.logic.num_words * self.logic.length
        len_paddings = len_snippet - len_words
        padding_size = int(len_paddings / (self.logic.num_words + 1))

        def generate_padding():
            return "".join([random.choice(padding_chars) for i in range(padding_size)])

        text = ""
        text += generate_padding()
        for word in self.logic.words:
            text += "".join([c for c in word])
            text += generate_padding()
        text += generate_padding()
        text = text[:len_snippet]
        return [text[i:i + self.colwidth] for i in range(0, len(text), self.colwidth)]

    def print_screen(self, history):
        """Redraw the entire terminal screen with the given content"""
        # Clear the terminal screen
        print()
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print screen contents
        print("ROBCO INDUSTRIES (TM) TERMALINK PROTOCOL\n" + \
              "ENTER PASSWORD NOW\n\n" + \
              str(self.logic.attempts) + " ATTEMPT(S) LEFT:" + (" █" * self.logic.attempts) + "\n")
        local_history = history[-self.rows + 1:]
        history_lines = ["" for i in range(self.rows - len(local_history) - 1)] + \
                        [">%s" % l for l in local_history] + [">"]
        for row in range(self.rows):
            # print address and text cells
            for column in range(self.columns):
                offset = self.rows * column
                index = offset + row
                print("%s %s  " % (self.hex_codes[index], self.code_snippet[index]), end="")
            print(history_lines[row], end="")
            if not row == self.rows - 1:
                print()

    def run(self):
        """Run the game main loop"""

        history = []

        self.print_screen(history)
        while self.logic.attempts != 0:
            guess = input().upper()
            history.append(guess)
            access, feedback = logic.check(guess)
            history.extend(feedback)
            self.print_screen(history)
            if access:
                break


if __name__ == '__main__':
    logic = NumberLogic(num_words=7, length=4, attempts=4)
    runner = GameRunner(logic)
    runner.run()
