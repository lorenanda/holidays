"""This program creates a GUI list for New Year resolutions."""

from tkinter import *

root = Tk()
root.title("New Year Resolutions")
root.geometry("500x500")

my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(
    my_frame,
    width=50,
    height=10,
    bg="#fff",
    bd=0,
    fg="#000",
    highlightthickness=0,
    selectbackground="yellow",
)
my_list.pack()

resolutions = ["get a job", "learn python", "rule the world"]

for resolution in resolutions:
    my_list.insert(END, resolution)


my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)


my_entry = Entry(root, font=("Helvetica", 10))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)


def delete_item():
    my_list.delete(ANCHOR)


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


def cross_item():
    my_list.itemconfig(my_list.curselection(), fg="#dedede")
    my_list.selection_clear(0, END)


def uncross_item():
    pass


delete_button = Button(button_frame, text="Delete", command=delete_item)
add_button = Button(button_frame, text="Add", command=add_item)
cross_button = Button(button_frame, text="Cross off", command=cross_item)
uncross_button = Button(button_frame, text="Uncross", command=uncross_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)

root.mainloop()
