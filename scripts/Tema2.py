import numpy as np


# Aici vom implementa clasa calculator
class Calculator(object):
    def __init__(self, x, y, operatii=None):
        """Constructorul primeste 2 numere,x si y"""
        # folosim self ca sa atribuim variabilelor din interiorul clasei
        self.x = x
        self.y = y
        self.operatii_valide = []
        if operatii is not None:
            for operatie in operatii:
                if operatie in ['+', '-', '*', '/','^2','radical','factorial']:
                    self.operatii_valide.append(operatie)

    def efectueaza_operatie(self, operatie):
        #Implementam lista cu operatii
        if operatie == '+':
            return self.adunare()
        elif operatie == '-':
            return self.scadere()
        elif operatie == '*':
            return self.inmultire()
        elif operatie == '/':
            return self.impartire()
        elif operatie == '^2':
            return self.patrat()
        elif operatie == 'radical':
            return self.radical()
        elif operatie == 'factorial':
            return self.factorial()

    # Implementam metoda care efectueaza toate operatiile
    def efectueaza_calcule(self):
        #Implementam lista cu operatii
        lista_rezultate = []
        for semn_operatie in self.operatii_valide:
            if semn_operatie == '+':
                lista_rezultate.append(self.adunare())
            elif semn_operatie == '-':
                lista_rezultate.append(self.scadere())
            elif semn_operatie == '*':
                lista_rezultate.append(self.inmultire())
            elif semn_operatie == '/':
                lista_rezultate.append(self.impartire())
            elif semn_operatie == '^2':
                lista_rezultate.append(self.patrat())
            elif semn_operatie == 'radical':
                lista_rezultate.append(self.radical())
            elif semn_operatie == 'factorial':
                lista_rezultate.append(self.factorial())
#Arata cum se calculeaza fiecare operatie
        return lista_rezultate
#este specificat cum se va realiza fiecare operatie
    def radical(self):
        rez = np.sqrt(self.x + self.y)
        return 'Rezultatul  {}'.format(rez)

    def patrat(self):
        rez = np.square(self.x + self.y)
        return 'Rezultatul  {}'.format(rez)

    def factorial(self):
        rez = np.math.factorial(self.x + self.y)
        return 'Rezultatul  {}'.format(rez)

    def adunare(self):
        rez = self.x + self.y
        return 'Rezultatul  {}'.format(rez)

    def scadere(self):
        rez = 0
        if self.x > self.y:
            rez = self.x - self.y
        elif self.x < self.y:
            rez = self.y - self.x
        return 'Rezultatul  {}'.format(rez)

    def inmultire(self):
        rez = self.x * self.y
        return 'Rezultatul  {}'.format(rez)

    def impartire(self):
        # Validam numerele
        rez = 0
        if self.x > self.y:
            rez = self.x / self.y
        elif self.x < self.y:
            rez = self.y / self.x
        return 'Rezultatul  {}'.format(rez)
#Am adaugat aceste doua comenzii de mai jos, este nevoie de ea
from Calculator import Calculator
if __name__ == '__main__':

#Am spus sa scrie 'Selectati operatia' si dupa am pus sa se aleaga ce semn de operatie vreau sa folosesc
    print("Selectati operatia :\n ")
    choice = input ("+, -, *, /, ^2, radical, factorial : \n")
    if choice in ('+', '-', '*', '/', '^2', 'radical', 'factorial'):
#Prin numar elemente lista , am intrebat cate numere va avea fiecare lista
#lista1 si lista2 le-am definit ca sa le pot folosi mai jos
        Numar_elemente_lista = input("Introduceti numarul de elemente: ")
        lista1 = []
        lista2 = []
        print("Introduceti elementele primei liste")
        for i in range(int(Numar_elemente_lista)):
#Am citit mai multe numere intr-o variabila, apoi le-am adunat in lista 1 ca la fiecare i sa se adune
#elementul dinainte cu cel nou, in acest fel am  stocat toate numerele in lista 1
            numar1 = [int(i) for i in input().split()]
            lista1 = lista1 + numar1
#Ca la primul FOR
        print("Introduceti elementele cele de a doua liste ")
        for i in range(int(Numar_elemente_lista)):
            numar2 = [int(i) for i in input().split()]
            lista2 = lista2 + numar2
#Daca semnul anterior este plus va face urmatorul set de instructiuni
        if choice == '+':
            cale_catre_fisier = "../dataset/Rezultate_tema2.txt"
            with open(cale_catre_fisier, "w") as fisier_scriere:
                operatii = '+'
#Acest for parcurge lista1 si lista2, el merge de la primul pana ultimul element din lista
                for i in range(len(lista1)):
                    x = int(lista1[i])
                    y = int(lista2[i])
                    calc = Calculator(x, y)
                    rezultat = calc.efectueaza_operatie(operatii)
                    calc = Calculator(x, y, operatii)
                    lista_calcule_rezultate = calc.efectueaza_calcule()
                    fisier_scriere.write("********************** \n")

                    fisier_scriere.write("Numar1: {}\n "
                                         "Numar2: {}\n".format(x, y))
                    fisier_scriere.write(" {} \n"

                                         .format(rezultat))
                    print('Sau scris rezultatele in fisier cu succes')

        elif choice == '-':
            cale_catre_fisier = "../dataset/Rezultate_tema2.txt"
            with open(cale_catre_fisier, "w") as fisier_scriere:
                operatii = '-'
                for i in range(len(lista1)):
                    x = int(lista1[i])
                    y = int(lista2[i])
                    calc = Calculator(x, y)

                    rezultat = calc.efectueaza_operatie(operatii)
                    calc = Calculator(x, y, operatii)
                    lista_calcule_rezultate = calc.efectueaza_calcule()
                    fisier_scriere.write("********************** \n")

                    fisier_scriere.write("Numar1: {}\n "
                                         "Numar2: {}\n".format(x, y))
                    fisier_scriere.write(" {} \n"

                                         .format(rezultat))

                    print('Sau scris rezultatele in fisier cu succes')

        elif choice == '*':
            cale_catre_fisier = "../dataset/Rezultate_tema2.txt"
            with open(cale_catre_fisier, "w") as fisier_scriere:

                operatii = '*'
                for i in range(len(lista1)):
                    x = int(lista1[i])
                    y = int(lista2[i])
                    calc = Calculator(x, y)

                    rezultat = calc.efectueaza_operatie(operatii)
                    calc = Calculator(x, y, operatii)
                    lista_calcule_rezultate = calc.efectueaza_calcule()
                    fisier_scriere.write("********************** \n")

                    fisier_scriere.write("Numar1: {}\n "
                                         "Numar2: {}\n".format(x, y))
                    fisier_scriere.write(" {} \n"

                                         .format(rezultat))

                    print('Sau scris rezultatele in fisier cu succes')

        elif choice == '/':
            cale_catre_fisier = "../dataset/Rezultate_tema2.txt"
            with open(cale_catre_fisier, "w") as fisier_scriere:

                operatii = '/'
                for i in range(len(lista1)):
                    x = int(lista1[i])
                    y = int(lista2[i])
                    calc = Calculator(x, y)

                    rezultat = calc.efectueaza_operatie(operatii)
                    calc = Calculator(x, y, operatii)
                    lista_calcule_rezultate = calc.efectueaza_calcule()
                    fisier_scriere.write("********************** \n")

                    fisier_scriere.write("Numar1: {}\n "
                                         "Numar2: {}\n".format(x, y))
                    fisier_scriere.write(" {} \n"

                                         .format(rezultat))

                    print('Sau scris rezultatele in fisier cu succes')

        elif choice == '^2':
            cale_catre_fisier = "../dataset/Rezultate_tema2.txt"
            with open(cale_catre_fisier, "w") as fisier_scriere:
                operatii = '^2'
                for i in range(len(lista1)):
                    x = int(lista1[i])
                    y = int(lista2[i])
                    calc = Calculator(x, y)
                    rezultat = calc.efectueaza_operatie(operatii)
                    calc = Calculator(x, y, operatii)
                    lista_calcule_rezultate = calc.efectueaza_calcule()
                    fisier_scriere.write("********************** \n")
                    fisier_scriere.write("Numar1: {}\n "
                                         "Numar2: {}\n".format(x, y))
                    fisier_scriere.write(" {} \n".format(rezultat))
                    print('Sau scris rezultatele in fisier cu succes')

        elif choice == 'radical':
            cale_catre_fisier = "../dataset/Rezultate_tema2.txt"
            with open(cale_catre_fisier, "w") as fisier_scriere:

                operatii = 'radical'
                for i in range(len(lista1)):
                    x = int(lista1[i])
                    y = int(lista2[i])
                    calc = Calculator(x, y)

                    rezultat = calc.efectueaza_operatie(operatii)
                    calc = Calculator(x, y, operatii)
                    lista_calcule_rezultate = calc.efectueaza_calcule()
                    fisier_scriere.write("********************** \n")

                    fisier_scriere.write("Numar1: {}\n "
                                         "Numar2: {}\n".format(x, y))
                    fisier_scriere.write(" {} \n"

                                         .format(rezultat))

                    print('Sau scris rezultatele in fisier cu succes')

        elif choice == 'factorial':
            cale_catre_fisier = "../dataset/Rezultate_tema2.txt"
            with open(cale_catre_fisier, "w") as fisier_scriere:

                operatii = 'factorial'
                for i in range(len(lista1)):
                    x = int(lista1[i])
                    y = int(lista2[i])
                    calc = Calculator(x, y)

                    rezultat = calc.efectueaza_operatie(operatii)
                    calc = Calculator(x, y, operatii)
                    lista_calcule_rezultate = calc.efectueaza_calcule()
                    fisier_scriere.write("********************** \n")

                    fisier_scriere.write("Numar1: {}\n "
                                         "Numar2: {}\n".format(x, y))
                    fisier_scriere.write("Factorial: {} \n"

                                         .format(rezultat))

                    print('Sau scris rezultatele in fisier cu succes')

    else:
        print("Invalid Input")












