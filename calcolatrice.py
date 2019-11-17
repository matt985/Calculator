from tkinter import *

class Calcolatrice:

    def __init__(self, parent):
        self.master = parent
        self.master.title("Calcolatrice")
        self.display = Entry(self.master, width=45, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.digits1 = []
        self.digits2 = []
        self.operation = ""
        self.risultato = None

        # definisci i bottoni

        self.button_1 = Button(self.master, text="1", padx=40, pady=20, command=lambda: self.button_click("1"))
        self.button_2 = Button(self.master, text="2", padx=40, pady=20, command=lambda: self.button_click("2"))
        self.button_3 = Button(self.master, text="3", padx=40, pady=20, command=lambda: self.button_click("3"))
        self.button_4 = Button(self.master, text="4", padx=40, pady=20, command=lambda: self.button_click("4"))
        self.button_5 = Button(self.master, text="5", padx=40, pady=20, command=lambda: self.button_click("5"))
        self.button_6 = Button(self.master, text="6", padx=40, pady=20, command=lambda: self.button_click("6"))
        self.button_7 = Button(self.master, text="7", padx=40, pady=20, command=lambda: self.button_click("7"))
        self.button_8 = Button(self.master, text="8", padx=40, pady=20, command=lambda: self.button_click("8"))
        self.button_9 = Button(self.master, text="9", padx=40, pady=20, command=lambda: self.button_click("9"))
        self.button_0 = Button(self.master, text="0", padx=95, pady=20, command=lambda: self.button_click("0"))
        self.button_comma = Button(self.master, text=",", padx=43, pady=20, command=lambda:self.button_click("."))

        self.button_add = Button(self.master, text="+", padx=38, pady=20, command=lambda:self.set_operation("+"))
        self.button_subtract = Button(self.master, text="-", padx=39, pady=20, command=lambda:self.set_operation("-"))
        self.button_mult = Button(self.master, text="*", padx=39, pady=20, command=lambda:self.set_operation("*"))
        self.button_divide = Button(self.master, text="/", padx=39, pady=20, command=lambda:self.set_operation("/"))

        self.button_equals = Button(self.master, text="=", padx=95, pady=20, command=lambda:self.calcola())
        self.button_reset = Button(self.master, text="Reset", padx=81, pady=20, command=lambda:self.reset())

        # posiziona i bottoni
        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)
        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)
        self.button_0.grid(row=4, column=0, columnspan=2)
        self.button_comma.grid(row=4, column=2)
                
        self.button_add.grid(row=4, column=3)
        self.button_subtract.grid(row=3, column=3)
        self.button_mult.grid(row=2, column=3)
        self.button_divide.grid(row=1, column=3)
        self.button_equals.grid(row=5, column=0, columnspan=2)
        self.button_reset.grid(row=5, column=2, columnspan=2)


    def button_click(self,num):
        # COMPORTAMENTO DISPLAY
        current_number = self.display.get()
        self.display.delete(0, END)
        self.display.insert(0, current_number + num)

        # COMPORTAMENTO COMPUTAZIONE
        if self.risultato == None:
            if self.operation == "":
                self.digits1.append(num)
                print(f"La lista 1 è ora {self.digits1}")
            else:
                self.digits2.append(num)
                print(f"La lista 2 è ora {self.digits2}")
        else:
            print(f"C'è già in memoria il risultato {self.risultato}")
            self.digits1.append(str(self.risultato))
            print(f"La lista 1 è ora {self.digits1}")
            self.digits2.append(num)
            print(f"La lista 2 è ora {self.digits2}")


    def genera_numero(self, lista_di_cifre):
        stringa_temp = ''.join(lista_di_cifre)
        numero = None
        if "." in stringa_temp:
            numero = float(stringa_temp)
        else:
            numero = int(stringa_temp)
        return numero


    def set_operation(self, str_operation):
        if str_operation == "+":
            self.operation = "+"
            self.display.delete(0, END)
        elif str_operation == "-":
            self.operation = "-"
            self.display.delete(0, END)
        elif str_operation == "*":
            self.operation = "*"
            self.display.delete(0, END)
        elif str_operation == "/":
            self.operation = "/"
            self.display.delete(0, END)


    def calcola(self):
        operando1 = self.genera_numero(self.digits1)
        self.digits1.clear()
        print(f"Ho generato il numero {operando1}")
        operando2 = self.genera_numero(self.digits2)
        self.digits2.clear()
        print(f"Ho generato il numero {operando2}")

        if self.operation == "+":
            self.risultato = operando1 + operando2
            self.operation = ""
        elif self.operation == "-":
            self.risultato = operando1 - operando2
            self.operation = ""
        elif self.operation == "*":
            self.risultato = operando1 * operando2
            self.operation = ""
        elif self.operation == "/":
            self.risultato = operando1 / operando2
            self.operation = ""

        self.display.delete(0, END)
        self.display.insert(0, self.risultato)


    def reset(self):
        self.display.delete(0, END)
        self.digits1.clear()
        self.digits2.clear()
        self.operation = ""
        self.risultato = None





if __name__ == "__main__":
    root = Tk()
    calc1 = Calcolatrice(root)
    root.mainloop()

