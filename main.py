import tkinter
from data.constants import *


# FUNCTIONS
def click(n):
    global operator
    # TODO: PERCENTAGE OPERATOR
    if operator != 0 or operator != "":
        operator = operator + str(n)
        text_input.set(operator)
        output.config(text=text_input)
    else:
        pass


def clear():
    global operator
    operator = ""
    text_input.set("")
    # TODO: OUTPUT
    output.config(text="")


def posOrMin():
    # TODO
    global operator
    operator = operator
    text_input.set(operator)
    output.config(text=text_input)


def mem():
    global memory, operator, mem_made
    if operator != "" and mem_made == 0:
        memory = operator
        clear()
        key_m.config(text="Mr")
        mem_made = 1
    else:
        click(memory)
        key_m.config(text="M")
        memory = ""
        mem_made = False


def equal():
    global operator, THEME
    try:
        if operator != "":
            sums = str(eval(operator))
            text_input.set(sums)
            operator = sums
            if operator == "1":
                # change_theme(1)
                print("Theme A")
            elif operator == "2":
                # change_theme(2)
                print("Theme B")
        else:
            pass
    except RuntimeError:
        text_input.set("Error")
    except SyntaxError:
        text_input.set("Error")
    except ZeroDivisionError:
        text_input.set("Error")
    finally:
        pass


# WINDOW
window = tkinter.Tk()
window.title('Python Calculator')
window.config(width=400, height=450, pady=20, padx=20, bg=L1_COLOUR)
window.minsize(width=400, height=450)
THEME = BLUE_THEME

# CALCULATE
operator = ""
text_input = tkinter.StringVar()
memory = ""
mem_made = 0

# OUTPUT LABEL
output = tkinter.Entry(textvariable=text_input,
                       font=OUTPUT_FONT,
                       justify="right",
                       borderwidth=2,
                       relief="groove",
                       background=L4_COLOUR)
output.grid(column=1, row=1, sticky='ew', columnspan=4)

# KEYS
key_m = tkinter.Button(
    text="M",
    bg=L5_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=OPERATOR_FONT,
    command=lambda: mem())
key_m.grid(column=1, row=2, sticky="NSEW")

key_c = tkinter.Button(
    text="C",
    bg=L5_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=OPERATOR_FONT,
    command=lambda: clear())
key_c.grid(column=2, row=2, sticky="NSEW")

key_percentage = tkinter.Button(
    text="%",
    bg=L5_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=OPERATOR_FONT,
    command=click("%"))
key_percentage.grid(column=3, row=2, sticky="NSEW")

key_div = tkinter.Button(
    text="➗",
    bg=L5_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=OPERATOR_FONT,
    command=lambda: click("/"))
key_div.grid(column=4, row=2, sticky="NSEW")

key_7 = tkinter.Button(
    text="7",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=lambda: click(7))
key_7.grid(column=1, row=3, sticky="NSEW")

key_8 = tkinter.Button(
    text="8",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=lambda: click(8))
key_8.grid(column=2, row=3, sticky="NSEW")

key_9 = tkinter.Button(
    text="9",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=lambda: click(9))
key_9.grid(column=3, row=3, sticky="NSEW")

key_multiply = tkinter.Button(
    text="✖",
    bg=L5_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=OPERATOR_FONT,
    command=lambda: click("*"))
key_multiply.grid(column=4, row=3, sticky="NSEW")

key_4 = tkinter.Button(
    text="4",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=lambda: click(4))
key_4.grid(column=1, row=4, sticky="NSEW")

key_5 = tkinter.Button(
    text="5",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=lambda: click(5))
key_5.grid(column=2, row=4, sticky="NSEW")

key_6 = tkinter.Button(
    text="6",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=lambda: click(6))
key_6.grid(column=3, row=4, sticky="NSEW")

key_add = tkinter.Button(
    text="➕",
    bg=L5_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=OPERATOR_FONT,
    command=lambda: click("+"))
key_add.grid(column=4, row=4, sticky="NSEW")

key_1 = tkinter.Button(
    text="1",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=lambda: click(1))
key_1.grid(column=1, row=5, sticky="NSEW")

key_2 = tkinter.Button(
    text="2",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=lambda: click(2))
key_2.grid(column=2, row=5, sticky="NSEW")

key_3 = tkinter.Button(
    text="3",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=lambda: click(3))
key_3.grid(column=3, row=5, sticky="NSEW")

key_subtract = tkinter.Button(
    text="➖",
    bg=L5_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=OPERATOR_FONT,
    command=lambda: click("-"))
key_subtract.grid(column=4, row=5, sticky="NSEW")

key_plusminus = tkinter.Button(
    text="+-",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=posOrMin())
key_plusminus.grid(column=1, row=6, sticky="NSEW")

key_0 = tkinter.Button(
    text="0",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=lambda: click(0))
key_0.grid(column=2, row=6, sticky="NSEW")

key_comma = tkinter.Button(
    text=",",
    bg=L2_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10, height=2,
    font=BUTTON_FONT,
    command=lambda: click("."))
key_comma.grid(column=3, row=6, sticky="NSEW")

key_equal = tkinter.Button(
    text="=",
    bg=L5_COLOUR,
    fg="white",
    activebackground=L3_COLOUR,
    activeforeground="white",
    relief="flat",
    bd=1,
    pady=5,
    width=10,
    font=OPERATOR_FONT,
    command=lambda: equal())
key_equal.grid(column=4, row=6, sticky="NSEW")

credit = tkinter.Label(text="created by Carel van der Merwe", bg=L1_COLOUR, fg='white', font=INFO_FONT)
credit.grid(column=1, row=7, columnspan=3, sticky='w')
copyright_label = tkinter.Label(text="@kalaharicarl ©2021", bg=L1_COLOUR, fg='white', font=INFO_FONT)
# copyright_label.grid(column=3, row=7, columnspan=2, sticky='e')

clear()

window.mainloop()
