class Calculator(object):
    def __init__(self, x, y, operatii):
        """Cintructorul pentru clasa cal"""
        self.x = x
        self.y = y
        self.operatii_valide = []
        for operatie in operatii:
            if operatie in ['+', '-', '*', '/']:
                self.operatii_valide.append(operatie)

    def efectueaza_calcule(self):
        # Trebuie sa implementam lista cu operatii
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
        return lista_rezultate


        
    def adunare(self):
        rez = self.x + self.y
        return 'Rezultatul operatiei de adunare este: {}'.format(rez)

    def scadere(self):
        rez=0
        if self.x >self.y:
            rez = self.x - self.y
        elif self.x < self.y:
            rez = self.y - self.x

        return 'Rezultatul operatiei de scadere este: {}'.format(rez)

    def inmultire(self):
        rez = self.x * self.y
        return "rezultatul operatitie de inmultire este: {}".format(rez)
    def impartire(self):
        rez=0
        if self.x > self.y:
            rez = self.x / self.y
        elif self.x < self.y:
            rez= self.y / self.x
        return 'rezultatul impartii este: {}'.format(rez)


