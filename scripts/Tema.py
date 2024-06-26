from Student import Student


print('Va rog introduceti ceea ce va este cerut in consola ,pentru a completa Registrul Studentilor')
print('Cati studenti doriti sa adaugati in registru ?')
nrelevi = input()
for i in range(int(nrelevi)):
    nume = input('Nume : ')
    prenume = input('Prenume : ')
    varsta = input('Varsta : ')
    sex = input('Sex(B pentru barbat sau F pentru femeie) :')
    anul = input("An : ")
    specializarea = input('Specializare : ')
    cale_catre_fisier = "../dataset/Rezultate Tema.txt"
    with open(cale_catre_fisier, "a") as fisier_scriere:
        fisier_scriere.write("**********************\n")
        fisier_scriere.write("Nume             {}\n".format(nume))
        fisier_scriere.write("Prenume          {}\n".format(prenume))
        fisier_scriere.write("Varsta           {}\n".format(varsta))
        fisier_scriere.write("Sex              {}\n".format(sex))
        fisier_scriere.write("An               {}\n".format(anul))
        fisier_scriere.write("Specializarea    {}\n".format(specializarea))
        print('Sa afisat partea 1')
        student = Student(nume , prenume ,varsta  , sex ,anul , specializarea )
        nrmaterii = input('Introduceti numarul de materii pe care le are specializarea precizata mai sus \n')
        for i in range(0,int(nrmaterii)):
            materie = input('Materie = ')
            note = [int(x) for x in input("Introduceti notele , pe aceasi linie , doar cu un spatiu intre ele: ").split()]
            materii = {materie:note}
            student.set_materii(materii)
            medii = student.calculeaza_medii()
            fisier_scriere.write("{} ".format(materie))
            note = (', '.join(map(str,note)))
            fisier_scriere.write(": {} |".format(note))
            fisier_scriere.write(" Medie {} \n".format(medii))
        print('Sa afisat partea 2')

        fisier_scriere.write("\n \n")



