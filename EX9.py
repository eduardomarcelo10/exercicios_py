#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.


if __name__ == '__main__':

    print("DIGITE A TEMPERATURA EM Fahrenheit:")
    fahrenheit = float(input ())

    resultado = (fahrenheit - 32) / 1.8

    print(f"Celsius: {resultado}")
