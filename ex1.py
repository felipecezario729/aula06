"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue 
pedindo até que o usuário informe um valor válido.
"""
try:
   
   while True:
     nota =  int(input('digite uma nota entre [0 e 10] '))
     if nota < 0 or nota > 10:
            print('Digite um valor valido')
     else:
        print('você digitou um valor valido')
        break 
except ValueError:
   print("digite um numero inteiro")  
            