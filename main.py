from tkinter import *

WHITE = ("#FFFFFF")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, background=WHITE)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(window, width=200, height=200, bg=WHITE, highlightthickness=0)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

# Labels
Label(window, text="Website:").grid(row=1, column=0, sticky="e")
Label(window, text="Email/Username:").grid(row=2, column=0, sticky="e")
Label(window, text="Password:").grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(window, width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1, sticky="w")

password_btn = Button(window, text="Generate Password")
password_btn.grid(row=3, column=2, sticky="w")

add_btn = Button(window, text="Add", width=36)
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")
window.mainloop()