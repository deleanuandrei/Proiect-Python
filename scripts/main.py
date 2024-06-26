from Calculator import Calculator


if __name__ == '__main__':
    print('Tastati 1 pentru adunare')

    x= input('x = ')
    y= input('y = ')

    operatii =['+', '-', '*', '/']
    calc = Calculator(int(x), int(y))

    rezultatul = calc.scadere()
    print(rezultatul)

    rezultatul = calc.impartire()
    print(rezultatul)

    rezultatul = calc.adunare()
    print(rezultatul)

    rezultatul = calc.inmultire()
    print(rezultatul)





