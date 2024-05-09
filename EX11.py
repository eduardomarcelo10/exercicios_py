#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A - o produto do dobro do primeiro com metade do segundo .
#B - a soma do triplo do primeiro com o terceiro.
#C -  terceiro elevado ao cubo

if __name__ == '__main__':

    print ("Digite um valor inteiro qualquer:")
    value1 = int(input ())

    print ("Digite um outro valor inteiro qualquer:")
    value2 = int(input ())

    print ("Digite um valor real qualquer:")
    value3 = float(input ())

    res1 = value1 * 2 + (value2/2)

    print (f"O resultado é: {res1}")

    res2 = (value1)*3 + value3

    print (f"O segundo resultado é: {res2}")

    res3 = (value3*value3*value3)

    print (f"O terceiro resultado é: {res3}")


