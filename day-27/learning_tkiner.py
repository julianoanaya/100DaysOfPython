from tkinter import *


def button_click():
    # my_label["text"] = "I got clicked"
    new_text = input.get()
    # my_label.config(text=input.get())
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# button
button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="new_button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)
# input.get()


window.mainloop()
