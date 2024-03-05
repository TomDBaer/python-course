import tkinter

window = tkinter.Tk()

window.title("Soxx my sock off")
window.minsize(width=500, height=300)
# padding
window.config(padx=20, pady=20)

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))

# button
def button_clicked():
    # Change text of label
    the_input = my_input.get()
    my_label.config(text="I got clicked")
    my_label.config(text=the_input)


my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button_2 = tkinter.Button(text="Touch me", command=button_clicked)


# Input
my_input = tkinter.Entry(width=10)

# Positionierung mit pack
""" my_button.pack()
my_input.pack()
my_label.pack() """

# Positionierung mit Place
""" 
my_label.place(x=0, y=0)
my_input.place(x=100, y=100)
"""

# Positionierung mit Grid // beste
my_label.grid(column=0, row=0)
my_button_2.grid(column=2, row=0)
my_button.grid(column=1, row=1)
my_input.grid(column=3, row=4)

# padding widget
my_label.config(padx= 10, pady=10)

# End of the program
window.mainloop()
