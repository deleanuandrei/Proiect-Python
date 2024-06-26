# Implementam clasa persoana
# : nume, prenume, varsta, sex
# : metode pentru printarea tuturor proprietatilor


class Persoana(object):
    # constructor
    def __init__(self, nume: str, prenume: str, varsta: int, sex: str):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.sex = sex

    def get_nume(self):
        return self.nume

    def get_prenume(self):
        return self.prenume

    def get_varsta(self):
        return self.varsta

    def get_sex(self):
        return self.sex
