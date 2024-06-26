#Definim doua nr
#efectuam calculele implementate in clasa noastra calculator

#salvam rezultatele in variabile separate
#deschidem un fisier txt
#scriem numerele in fisier
#pe fiecare linie in parte, scriem rezultatele operatiilor
#*******************************
#NUmar1 = {}
#Numar2 = {}
#Adunare: Rezultatul adunarii este egal cu {}

from Calculator import Calculator
if __name__ == '__main__':
    x = 25
    y = 40

    operatii = ["+", "-", "*", "/"]
    calc = Calculator(x, y, operatii)
    lista_calcule_rezultate = calc.efectueaza_calcule()


    #Umpacking
    rez_adunare, rez_scadere, rez_inmultire, rez_impartire = lista_calcule_rezultate

    cale_catre_fisier = "dataset/rezultate.txt"
    with open(cale_catre_fisier, "w") as fisier_scriere:
        fisier_scriere.write("************************************** \n")
        fisier_scriere.write("Numar1: {} \n"
                             "Numar2: {} \n".format(x, y))
        fisier_scriere.write("Adunare: {} \n"
                             "Scadere: {} \n"
                             "Inmultire: {} \n"
                             "Impartire: {} \n".format(rez_adunare, rez_scadere, rez_inmultire, rez_impartire))
        fisier_scriere.write("==================== \n")
    print('S-au scris rezultatele in fisier cu success.')
