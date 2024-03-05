import tkinter
""" 
Benötige 4 label
1 input
1 button
"""

window = tkinter.Tk()
window.geometry("300x200")
window.resizable(False, False)
#window.config(width=300, height=200)
window.config(padx=15, pady=15)
window.title("This is a calculator")


# Logic
value = tkinter.StringVar()
conversion_rate = 1.609

def calculate():
    new_value = float(value.get()) * conversion_rate
    miles_text3.config(text=new_value)


miles_text1 = tkinter.Label(text="Miles")
miles_text2 = tkinter.Label(text="is equal to")
miles_text3 = tkinter.Label(text=0)
miles_text4 = tkinter.Label(text="Km")

my_input = tkinter.Entry(textvariable=value)


calculate_button = tkinter.Button(text="Calculate", command=calculate)

# Grid building
my_input.grid(column=1, row=0)
miles_text1.grid(column=2, row=0)
miles_text2.grid(column=0, row=1)
miles_text3.grid(column=1, row=1)
miles_text4.grid(column=2, row=1)
calculate_button.grid(column=1, row=2)




window.mainloop()