# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)

canvas.grid(column=1, row=0, padx=20, pady=20)

# Inputs
# Website
website_label = Label()
website_label.config(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.config(width=35)
website_input.grid(column=1, row=1, columnspan=2)

# Email/Username
email_label = Label()
email_label.config(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)

email_input = Entry()
email_input.config(width=35)
email_input.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label()
password_label.config(text="Password:", bg="white")
password_label.grid(column=0, row=3)

password_input = Entry()
password_input.config(width=21)
password_input.grid(column=1, row=3)


# Button
# Generate PW
generate_button = Button()
generate_button.config(text="Generate Password")
generate_button.grid(column=2, row=3)

# Add
add_button = Button()
add_button.config(text="Add", width=32)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()