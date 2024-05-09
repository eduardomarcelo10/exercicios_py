#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

if __name__ == '__main__':

    print("DIGITE A TEMPERATURA EM CELSIUS:")
    celsius = float(input ())

    resultado = (celsius * 1.8) + 32

    print(f"Celsius: {resultado}")
