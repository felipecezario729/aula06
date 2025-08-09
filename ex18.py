"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

"""
qtnumero = int(input('digite a quantidade de numeros'))
lista = []
for i in range(qtnumero):
    numero = int(input(f'digite o {i+1} numero'))
    lista.append(numero)
print(lista)   

    