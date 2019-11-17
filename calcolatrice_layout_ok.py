from tkinter import *

root = Tk()
root.title("Calcolatrice")
display = Entry(root, width=45, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

digits1 = []
digits2 = []
operation = ""
output = None


def button_click(num):
    # senza display.get() la calcolatrice inserirebbe a display i numeri al contrario
    current_number = display.get()
    display.delete(0, END)
    display.insert(0, current_number + num)

def reset():
    display.delete(0, END)


# definisci i bottoni

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click("1"))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click("2"))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click("3"))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click("4"))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click("5"))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click("6"))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click("7"))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click("8"))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click("9"))
button_0 = Button(root, text="0", padx=95, pady=20, command=lambda: button_click("0"))
button_comma = Button(root, text=",", padx=43, pady=20, command=lambda:button_click("."))

button_add = Button(root, text="+", padx=38, pady=20, command=lambda:set_operation("+"))
button_subtract = Button(root, text="-", padx=39, pady=20, command=lambda:set_operation("-"))
button_mult = Button(root, text="*", padx=39, pady=20, command=lambda:set_operation("*"))
button_divide = Button(root, text="/", padx=39, pady=20, command=lambda:set_operation("/"))

button_equals = Button(root, text="=", padx=95, pady=20, command=lambda:compute())
button_reset = Button(root, text="Reset", padx=81, pady=20, command=reset)









##

# button_add = Button(root, text="+", padx=39, pady=20, command=lambda:button_click())
# button_equals = Button(root, text="=", padx=99, pady=20,)
# button_reset = Button(root, text="Reset", padx=86, pady=20, command=button_reset)

# disponi i bottoni sullo schermo (ordine invertito)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0, columnspan=2)
button_comma.grid(row=4, column=2)
        

button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_mult.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
button_equals.grid(row=5, column=0, columnspan=2)
button_reset.grid(row=5, column=2, columnspan=2)



root.mainloop()

