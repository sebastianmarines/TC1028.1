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
            ImageTk.PhotoImage(Image.open(f"images/hang{n}.png")) for n in range(11)
        ]
        img_label = Label(self.root)
        img_label.grid(row=4, column=1, columnspan=3, padx=10, pady=40)
        img_label.config(image=self.images[10])

        text_label = Label(self.root)
        ft = tkFont.Font(family="Times", size=30)
        text_label.grid(row=5, column=5, columnspan=10)
        text_label.config(font=ft)

        self._load_words()

        text_label.config(text=random.choice(self.words))

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

    def guess(self, letter):
        button = self.buttons[letter]
        button["state"] = tk.DISABLED
        button.configure(
            bg="Gray", fg="white", activebackground="Gray", activeforeground="white"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
