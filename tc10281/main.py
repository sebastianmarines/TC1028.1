import tkinter as tk
import tkinter.font as tkFont
from tkinter import Button
from string import ascii_uppercase


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting root size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        n = 13
        letter_groups = [
            ascii_uppercase[i : i + n] for i in range(0, len(ascii_uppercase), n)
        ]
        self.buttons = {}
        for i, group in enumerate(letter_groups, start=1):
            for j, letter in enumerate(group, start=1):
                _button = Button(
                    root,
                    text=letter,
                    bg="skyBlue",
                    fg="Black",
                    width=2,
                    height=1,
                    font=("Helvetica", "20"),
                    command=lambda letter=letter: self.guess(letter),
                )
                _button.grid(column=j, row=i)
                self.buttons[letter] = _button

    def guess(self, letter):
        self.buttons[letter].configure(bg="Gray", fg="white")
        print(letter)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
