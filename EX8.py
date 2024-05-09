#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

#PROGRAMA INICIAL

if __name__ == '__main__':

    print("DIGITE O VALOR DA HORA TRABALHADA:")
    valor_hora = float(input ())

    print("DIGITE O NUMERO DE HORAS TRABALHADAS:")
    horas = float(input ())

    resultado = valor_hora * horas

    print(f"O resultado é: {resultado}")
