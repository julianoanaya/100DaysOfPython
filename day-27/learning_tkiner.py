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

button = Button(text="Click Me")
button.pack()

window.mainloop()
