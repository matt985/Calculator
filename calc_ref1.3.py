from tkinter import *
from aux_modulo_calc import *

class Calcolatrice:

    def __init__(self, parent):

        self.genitore = parent
        parent.title("Calcolatrice 1.3")


        # GENERAZIONE CONTENITORE e COSTANTI DI CONTROLLO DISPOSIZIONE
        larghezza_pulsanti = 4                  # in pixel
        imb_pulsantex = "2m"                    # in millimetri (imbottitura pulsante asse orizzontale)
        imb_pulsantey = "2m"                    # in millimetri (imbottitura pulsante asse verticale)
        imb_contenitorex = "3m"
        imb_contenitorey = "3m"
        imb_interna_contenitorex = "3m"
        imb_interna_contenitorey = "3m"


        self.contenitore = Frame(parent)
        self.contenitore.pack(
            ipadx = imb_interna_contenitorex,
            ipady = imb_interna_contenitorey,
            padx = imb_contenitorex,
            pady = imb_contenitorey,
            )


        # VARIABILI DI SERVIZIO
        self.digits_num1 = []
        self.digits_num2 = []
        self.operation = ''
        self.risultato = None


        # DIGITS BUTTONS
        self.button1 = Button(self.contenitore, command= self.button1Premuto)
        self.button1.configure(text="1", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button1.grid(row=0, column=0)

        self.button2 = Button(self.contenitore, command= self.button2Premuto)
        self.button2.configure(text="2", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button2.grid(row=0, column=1)

        self.button3 = Button(self.contenitore, command= self.button3Premuto)
        self.button3.configure(text="3", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button3.grid(row=0, column=2)

        self.button4 = Button(self.contenitore, command= self.button4Premuto)
        self.button4.configure(text="4", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button4.grid(row=1, column=0)

        self.button5 = Button(self.contenitore, command= self.button5Premuto)
        self.button5.configure(text="5", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button5.grid(row=1, column=1)

        self.button6 = Button(self.contenitore, command= self.button6Premuto)
        self.button6.configure(text="6", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button6.grid(row=1, column=2)

        self.button7 = Button(self.contenitore, command= self.button7Premuto)
        self.button7.configure(text="7", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button7.grid(row=2, column=0)

        self.button8 = Button(self.contenitore, command= self.button8Premuto)
        self.button8.configure(text="8", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button8.grid(row=2, column=1)

        self.button9 = Button(self.contenitore, command= self.button9Premuto)
        self.button9.configure(text="9", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button9.grid(row=2, column=2)

        self.button0 = Button(self.contenitore, command= self.button0Premuto)
        self.button0.configure(text="0", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button0.grid(row=3, column=1)

        self.button_comma = Button(self.contenitore, command = self.button_comma_Premuto)
        self.button_comma.configure(text=".", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button_comma.grid(row=3, column=2)


        # OPERATION BUTTONS
        self.button_add = Button(self.contenitore, command= self.button_add_premuto)
        self.button_add.configure(text="+", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button_add.grid(row=0, column=3)

        self.button_subtract = Button(self.contenitore, command= self.button_subtract_premuto)
        self.button_subtract.configure(text="-", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button_subtract.grid(row=1, column=3)

        self.button_mult = Button(self.contenitore, command= self.button_mult_premuto)
        self.button_mult.configure(text="*", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button_mult.grid(row=2, column=3)

        self.button_divide = Button(self.contenitore, command= self.button_divide_premuto)
        self.button_divide.configure(text="/", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button_divide.grid(row=3, column=3)

        self.button_result = Button(self.contenitore, command= self.button_result_premuto)
        self.button_result.configure(text="=", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.button_result.grid(row=3, column =0)

        # UTILITY & DEBUG BUTTONS
        self.abort_button = Button(self.contenitore, command = self.pulsante_abort_premuto)
        self.abort_button.configure(text="Abort", width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
        self.abort_button.grid(row=4, column=1)


    # GESTIONE OGGETTI EVENTO
    # Gestione pressione pulsanti cifre

    def button1Premuto(self):
        print("Premuto: 1")
        if not self.operation:
            self.digits_num1.append("1")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
            label1 = Label(self.contenitore, text=self.digits_num1)
            label1.grid(row=5, column=1)
        else:
            self.digits_num2.append("1")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")
            label1 = Label(self.contenitore, text=self.digits_num2)
            label1.grid(row=5, column=1)


    def button2Premuto(self):
        print("Premuto: 2")
        if not self.operation:
            self.digits_num1.append("2")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
            label2 = Label(self.contenitore, text=self.digits_num1)
            label2.grid(row=5, column=1)
        else:
            self.digits_num2.append("2")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")
            label2 = Label(self.contenitore, text=self.digits_num2)
            label2.grid(row=5, column=1)


    def button3Premuto(self):
        print("Premuto: 3")
        if not self.operation:
            self.digits_num1.append("3")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
            label3 = Label(self.contenitore, text=self.digits_num1)
            label3.grid(row=5, column=1)
        else:
            self.digits_num2.append("3")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")
            label3 = Label(self.contenitore, text=self.digits_num2)
            label3.grid(row=5, column=1)


    def button4Premuto(self):
        print("Premuto: 4")
        if not self.operation:
            self.digits_num1.append("4")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
            label4 = Label(self.contenitore, text=self.digits_num1)
            label4.grid(row=5, column=1)
        else:
            self.digits_num2.append("4")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")
            label4 = Label(self.contenitore, text=self.digits_num2)
            label4.grid(row=5, column=1)


    def button5Premuto(self):
        print("Premuto: 5")
        if not self.operation:
            self.digits_num1.append("5")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
            label5 = Label(self.contenitore, text=self.digits_num1)
            label5.grid(row=5, column=1)
        else:
            self.digits_num2.append("5")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")
            label5 = Label(self.contenitore, text=self.digits_num2)
            label5.grid(row=5, column=1)


    def button6Premuto(self):
        print("Premuto: 6")
        if not self.operation:
            self.digits_num1.append("6")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
            label6 = Label(self.contenitore, text=self.digits_num1)
            label6.grid(row=5, column=1)
        else:
            self.digits_num2.append("6")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")
            label6 = Label(self.contenitore, text=self.digits_num2)
            label6.grid(row=5, column=1)


    def button7Premuto(self):
        print("Premuto: 7")
        if not self.operation:
            self.digits_num1.append("7")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
            label7 = Label(self.contenitore, text=self.digits_num1)
            label7.grid(row=5, column=1)
        else:
            self.digits_num2.append("7")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")
            label7 = Label(self.contenitore, text=self.digits_num2)
            label7.grid(row=5, column=1)


    def button8Premuto(self):
        print("Premuto: 8")
        if not self.operation:
            self.digits_num1.append("8")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
            label8 = Label(self.contenitore, text=self.digits_num1)
            label8.grid(row=5, column=1)
        else:
            self.digits_num2.append("8")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")
            label8 = Label(self.contenitore, text=self.digits_num2)
            label8.grid(row=5, column=1)


    def button9Premuto(self):
        print("Premuto: 9")
        if not self.operation:
            self.digits_num1.append("9")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
            label9 = Label(self.contenitore, text=self.digits_num1)
            label9.grid(row=5, column=1)
        else:
            self.digits_num2.append("9")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")
            label9 = Label(self.contenitore, text=self.digits_num2)
            label9.grid(row=5, column=1)


    def button0Premuto(self):
        print("Premuto: 0")
        if not self.operation:
            self.digits_num1.append("0")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
            label0 = Label(self.contenitore, text=self.digits_num1)
            label0.grid(row=5, column=1)
        else:
            self.digits_num2.append("0")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")
            label0 = Label(self.contenitore, text=self.digits_num2)
            label0.grid(row=5, column=1)


    def button_comma_Premuto(self):
        print("Premuto: .")
        if not self.operation:
            self.digits_num1.append(".")
            print(f"La lista cifre 1 è ora questa: {self.digits_num1}")
            label_comma = Label(self.contenitore, text=self.digits_num1)
            label_comma.grid(row=5, column=1)
        else:
            self.digits_num2.append(".")
            print(f"La lista cifre 2 è ora questa: {self.digits_num2}")
            label_comma = Label(self.contenitore, text=self.digits_num2)
            label_comma.grid(row=5, column=1)


    # Gestione pressione pulsanti di operazione

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

        label = Label(self.contenitore, text=self.risultato)
        label.grid(row=5, column=1)


    # Gestione pressione pulsanti utility & debug

    def pulsante_abort_premuto(self):
        print("Aborting now...")
        self.genitore.destroy()



# FINE main script

if __name__ == '__main__':
    root = Tk()
    calc1 = Calcolatrice(root)
    root.mainloop()