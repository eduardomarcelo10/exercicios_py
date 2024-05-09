#PROGRAMA INICIAL
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

if __name__ == '__main__':


    print ("Digite as notas bimestrais do aluno:")
    print ("nota1:")
    nota1 = float(input ())
    print ("nota2:")
    nota2 = float(input ())
    print ("nota3:")
    nota3 = float(input ())
    print ("nota4:")
    nota4 = float(input ())

    media = (nota1+nota2+nota3+nota4)/4

    print (f"A media do aluno é:{media}")
