from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=500, height=300)


def button_clicked():
    miles = float(miles_enter.get())
    km = miles * 1.609
    convert_to_km_label.config(text=f"{km}")


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

convert_to_km_label = Label(text="output")
convert_to_km_label.grid(column=1, row=1)

miles_enter = Entry(width=10)
miles_enter.grid(column=1, row=0)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)
window.mainloop()
