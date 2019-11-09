
def genera_numero_da_lista_di_cifre(lista):
    """
    Prende una lista che rappresenta le cifre di un numero e le converte
    in numero vero e proprio (float o int) 
    """
    stringa = ''.join(lista)
    numero = None
    if '.' in stringa:
        numero = float(stringa)
    else:
        numero = int(stringa)
    return numero






if __name__ == '__main__':
    lista = list(input('-> '))
    genera_numero_da_lista_di_cifre(lista)


