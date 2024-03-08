from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# button


def button_click():
    # my_label["text"] = "I got clicked"
    new_text = input.get()
    # my_label.config(text=input.get())
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_click)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
# input.get()
print(input.get())
window.mainloop()
