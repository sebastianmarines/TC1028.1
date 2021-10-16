import random
import tkinter as tk
import tkinter.font as tkFont
from string import ascii_uppercase
from tkinter import Button, Canvas, Label

from PIL import Image, ImageTk


class App:
    def __init__(self, root):
        self.buttons = {}
        self.words = list()
        self.root = root

        self.chosen_word = []
        self.guessed_word = []

        self.guesses = 0

        # setting title
        self.root.title("Juego del ahorcado")
        # setting self.root size
        width = 800
        height = 500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        self.root.geometry(alignstr)
        self.root.resizable(width=True, height=True)

        self.canvas = Canvas(self.root)

        self._configure_buttons()

        self.images = [
            ImageTk.PhotoImage(Image.open(f"images/hang{n}.png")) for n in range(12)
        ]
        self.img_label = Label(self.root)
        self.img_label.grid(row=4, column=1, columnspan=3, padx=10, pady=40)
        self.img_label.config(image=self.images[0])

        self.text_label = Label(self.root)
        ft = tkFont.Font(family="Times", size=30)
        self.text_label.grid(row=5, column=5, columnspan=10)
        self.text_label.config(font=ft)

        self._load_words()
        self._set_word()

    def _configure_buttons(self):
        n = 13
        letter_groups = [
            ascii_uppercase[i : i + n] for i in range(0, len(ascii_uppercase), n)
        ]
        for i, group in enumerate(letter_groups, start=1):
            for j, letter in enumerate(group, start=1):
                _button = Button(
                    self.root,
                    text=letter,
                    bg="skyBlue",
                    fg="Black",
                    activebackground="skyBlue",
                    activeforeground="Black",
                    width=2,
                    height=1,
                    font=("Helvetica", "20"),
                    command=lambda letter=letter: self.guess(letter),
                )
                _button.grid(column=j, row=i)
                self.buttons[letter] = _button

    def _load_words(self):
        with open("palabras.txt") as file:
            self.words = [line.strip("\n") for line in file.readlines()]

    def _set_word(self):
        self.chosen_word = list(random.choice(self.words))
        self.guessed_word = list("_" * len(self.chosen_word))
        self._update_word()

    def _update_word(self):
        self.text_label.config(text=" ".join(self.guessed_word))

    def guess(self, button):
        correct = False
        for i, letter in enumerate(self.chosen_word):
            if letter == button:
                correct = True
                self.guessed_word[i] = letter

        self._update_word()

        if not correct:
            self.guesses += 1
            self.img_label.config(image=self.images[self.guesses])

        button = self.buttons[button]
        button["state"] = tk.DISABLED
        button.configure(
            bg="Gray", fg="white", activebackground="Gray", activeforeground="white"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
