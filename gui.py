import tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, Label

import congen as cg


def generate_name_btn_clicked():
    keys_num = int(keys_num_input.get())
    names_num = int(words_num_input.get())

    cg.concatenator.generate_random(cg.default_lang, cg.Word(keys_num, names_num))
    display_names()


def display_names():
    show_up = str(cg.concatenator.words_output)
    names_display = Text(master=window, height=10, width=30, bg='#EDDECC', font=("Bitter", 11), relief='flat')
    names_display.place(x=220, y=138, width=454, height=188)
    names_display.insert(tkinter.END, show_up)


window = Tk()
window.title('old CREATOR')

window.geometry("740x400")
window.configure(bg="#D3B890")


canvas = Canvas(
    window,
    bg="#D3B890",
    height=400,
    width=740,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

keys_num_input = Entry(
    bd=0,
    bg="#EDDECC",
    fg="#000716",
    highlightthickness=0
)
keys_num_input.place(
    x=55.0,
    y=184.0,
    width=45.0,
    height=22.0
)

words_num_input = Entry(
    bd=0,
    bg="#EDDECC",
    fg="#000716",
    highlightthickness=0
)
words_num_input.place(
    x=134.0,
    y=184.0,
    width=45.0,
    height=22.0
)

generate_name_btn = Button(
    bg='#453E30',
    fg='#EDDECC',
    text='Generate!',
    font=('Bitter', 12),
    borderwidth=0,
    highlightthickness=0,
    command=generate_name_btn_clicked,
    relief="raised"
)
generate_name_btn.place(
    x=55.0,
    y=224.0,
    width=124.0,
    height=48.0
)

canvas.create_rectangle(
    216.0,
    128.0,
    674.0,
    332.0,
    fill="#EDDECC",
    outline="")

# noinspection PyTypeChecker
output_label = Label(window, text=display_names(), anchor='nw')
output_label.grid()

canvas.create_text(
    58.0,
    153.0,
    anchor="nw",
    text="Keys",
    fill="#453E30",
    font=("Bitter", 12)
)

canvas.create_text(
    132.0,
    153.0,
    anchor="nw",
    text="Words",
    fill="#453E30",
    font=("Bitter", 12)
)

canvas.create_text(
    134.0,
    66.0,
    anchor="nw",
    text="PRIMITIVE WORD CONCATENATOR",
    fill="#453E30",
    font=("Bitter", 20)
)

canvas.create_text(
    70.0,
    118.0,
    anchor="nw",
    text="SETTINGS",
    fill="#453E30",
    font=("Bitter", 16)
)

window.resizable(False, False)
window.mainloop()
