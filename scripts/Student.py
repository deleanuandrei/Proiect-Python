# Implementam clasa student
# : lista note
# : lista materii

from Persoana import Persoana


class Student(Persoana):
    def __init__(self, nume, prenume, varsta, sex, specializarea: str, anul: int):
        Persoana.__init__(self, nume, prenume, varsta, sex)
        self.specializarea = specializarea
        self.anul = anul
        self.materii = {}

    def get_specializarea(self):
        return self.specializarea

    def get_anul(self):
        return self.anul

    def set_materii(self, lista_materii):
        self.materii = lista_materii


    def __repr__(self):
        return 'Studentul cu numele : {}, sex: {}, varsta de: {}, este in anul: {}, la specializarea: {}'.format(
            self.nume + ' ' + self.prenume,
            self.sex,
            self.varsta,
            self.anul,
            self.specializarea
        )

    def calculeaza_medii(self):
        rez = {}
        for materie in self.materii.keys():
            note = self.materii[materie]
            media = sum(note) / len(note)
            rez = media
        return rez