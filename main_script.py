from tkinter import *
from aux_modulo_calc import *

class Calcolatrice:

    def __init__(self, parent):
        self.genitore = parent
        self.contenitore = Frame(parent)
        self.contenitore.pack()

        self.digits_num1 = []
        self.operation = ''
        self.digits_num2 = []
        self.risultato = None

        # DIGITS BUTTONS
        self.button1 = Button(self.contenitore, command= self.button1Premuto)
        self.button1.configure(text="1")
        self.button1.grid(row=0, column=0)

        self.button2 = Button(self.contenitore, command= self.button2Premuto)
        self.button2.configure(text="2")
        self.button2.grid(row=0, column=1)

        self.button3 = Button(self.contenitore, command= self.button3Premuto)
        self.button3.configure(text="3")
        self.button3.grid(row=0, column=2)

        self.button4 = Button(self.contenitore, command= self.button4Premuto)
        self.button4.configure(text="4")
        self.button4.grid(row=1, column=0)

        self.button5 = Button(self.contenitore, command= self.button5Premuto)
        self.button5.configure(text="5")
        self.button5.grid(row=1, column=1)

        self.button6 = Button(self.contenitore, command= self.button6Premuto)
        self.button6.configure(text="6")
        self.button6.grid(row=1, column=2)

        self.button7 = Button(self.contenitore, command= self.button7Premuto)
        self.button7.configure(text="7")
        self.button7.grid(row=2, column=0)

        self.button8 = Button(self.contenitore, command= self.button8Premuto)
        self.button8.configure(text="8")
        self.button8.grid(row=2, column=1)

        self.button9 = Button(self.contenitore, command= self.button9Premuto)
        self.button9.configure(text="6")
        self.button9.grid(row=2, column=2)

        self.button0 = Button(self.contenitore, command= self.button0Premuto)
        self.button0.configure(text="0")
        self.button0.grid(row=3, column=1)

        self.button_comma = Button(self.contenitore, command = self.button_comma_Premuto)
        self.button_comma.configure(text=".")
        self.button_comma.grid(row=3, column=2)


        # OPERATION BUTTONS
        self.button_add = Button(self.contenitore, command= self.button_add_premuto)
        self.button_add.configure(text="+")
        self.button_add.grid(row=0, column=3)

        self.button_subtract = Button(self.contenitore, command= self.button_subtract_premuto)
        self.button_subtract.configure(text="-")
        self.button_subtract.grid(row=1, column=3)

        self.button_mult = Button(self.contenitore, command= self.button_mult_premuto)
        self.button_mult.configure(text="*")
        self.button_mult.grid(row=2, column=3)

        self.button_divide = Button(self.contenitore, command= self.button_divide_premuto)
        self.button_divide.configure(text="/")
        self.button_divide.grid(row=3, column=3)

        self.button_result = Button(self.contenitore, command= self.button_result_premuto)
        self.button_result.configure(text="=")
        self.button_result.grid(row=3, column =0)





        # UTILITY BUTTONS
        self.abort_button = Button(self.contenitore, command = self.pulsante_abort_premuto)
        self.abort_button.configure(text="Abort")
        self.abort_button.grid(row=4, column=3)




    # GESTIONE OGGETTI EVENTO
    # Gestione pressione pulsanti cifre

    def button1Premuto(self):
        print("Premuto: 1")
        if not self.operation:
            self.digits_num1.append("1")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
        else:
            self.digits_num2.append("1")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")

    def button2Premuto(self):
        print("Premuto: 2")
        if not self.operation:
            self.digits_num1.append("2")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
        else:
            self.digits_num2.append("2")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")

    def button3Premuto(self):
        print("Premuto: 3")
        if not self.operation:
            self.digits_num1.append("3")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
        else:
            self.digits_num2.append("3")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")

    def button4Premuto(self):
        print("Premuto: 4")
        if not self.operation:
            self.digits_num1.append("4")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
        else:
            self.digits_num2.append("4")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")


    def button5Premuto(self):
        print("Premuto: 5")
        if not self.operation:
            self.digits_num1.append("5")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
        else:
            self.digits_num2.append("5")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")


    def button6Premuto(self):
        print("Premuto: 6")
        if not self.operation:
            self.digits_num1.append("6")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
        else:
            self.digits_num2.append("6")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")



    def button7Premuto(self):
        print("Premuto: 7")
        if not self.operation:
            self.digits_num1.append("7")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
        else:
            self.digits_num2.append("7")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")


    def button8Premuto(self):
        print("Premuto: 8")
        if not self.operation:
            self.digits_num1.append("8")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
        else:
            self.digits_num2.append("8")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")


    def button9Premuto(self):
        print("Premuto: 9")
        if not self.operation:
            self.digits_num1.append("9")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
        else:
            self.digits_num2.append("9")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")


    def button0Premuto(self):
        print("Premuto: 0")
        if not self.operation:
            self.digits_num1.append("0")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
        else:
            self.digits_num2.append("0")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")

    def button_comma_Premuto(self):
        print("Premuto: .")
        if not self.operation:
            self.digits_num1.append(".")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
        else:
            self.digits_num2.append(".")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")


    # Gestione pulsanti operazioni

    def button_add_premuto(self):
        print("Premuto: +")
        self.operation = "+"
        print(f"Impostata operazione: {self.operation} ")

    def button_subtract_premuto(self):
        print("Premuto: -")
        self.operation = "-"
        print(f"Impostata operazione: {self.operation}")

    def button_mult_premuto(self):
        print("Premuto: *")
        self.operation = "*"
        print(f"Impostata operazione: {self.operation}")

    def button_divide_premuto(self):
        print("Premuto: /")
        self.operation = "/"
        print(f"Impostata operazione: {self.operation}")

    def button_result_premuto(self):
        print("Premuto: =")
        num1 = genera_numero_da_lista_di_cifre(self.digits_num1)
        print(f"Ho generato: {num1}")
        self.digits_num1.clear()                                    
        num2 = genera_numero_da_lista_di_cifre(self.digits_num2)
        print(f"Ho generato: {num2}")
        self.digits_num2.clear()

        print("Determino il tipo di operazione")
        if self.operation == "+":
            print(f"Il risultato è {num1 + num2}")                      
            self.risultato = num1 + num2
            self.operation = ""
        elif self.operation == "-":
            print(f"Il risultato è {num1 - num2}")
            self.risultato = num1 - num2
            self.operation = ""
        elif self.operation == "*":
            print(f"Il risultato è {num1 * num2}")
            self.risultato = num1 * num2
            self.operation = ""
        elif self.operation =="/":
            print(f"Il risultato è {num1 / num2}")
            self.risultato = num1 / num2
            self.operation = ""



    # Gestione pulsanti utility

    def pulsante_abort_premuto(self):
        print("Aborting now...")
        self.genitore.destroy()





if __name__ == '__main__':
    root = Tk()
    calc1 = Calcolatrice(root)
    root.mainloop()