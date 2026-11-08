from tkinter import *
# TODO: Create an UI with logo in middle, a black square around it.

WHITE = ("#FFFFFF")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, background=WHITE)

canvas = Canvas(window, width=200, height=200, bg=WHITE, highlightthickness=0)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.pack()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window.mainloop()