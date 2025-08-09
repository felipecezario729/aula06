"""
 Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
Faça um programa que leia uma lista de 10 numeros. exemplo
"""
qtnumero = int(input('digite a quantidade de numeros'))
lista = []
for i in range(4):
    numero = int(input(f'digite o {i+1} numero'))
    lista.append(numero)
print('ordem e entrada')        
print(lista)
print('ordem inversa')
lista.reverse()
print(lista)
print('valor maximo ')
print(f'maximo {max(lista)}')
print('valor Minimo')
print(f'minimo {min(lista)}')

  
