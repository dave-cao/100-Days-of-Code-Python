from tkinter import *

FONT = ("Courier", 24)

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)


def convert():
    miles = int(miles_input.get())
    km = miles * 1.609

    KM_number.config(text=f"{round(km, 2)}")


# 1. input for miles
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
# 2. label for miles
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
# 3. label for "is equal to"
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)
# 4. input for KM
KM_number = Label(text=0, font=FONT)
KM_number.grid(column=1, row=1)
# 5. label for km
KM_label = Label(text="KM", font=FONT)
KM_label.grid(column=2, row=1)
# - calcualte button
calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)


window.mainloop()
