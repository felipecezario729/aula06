"""
Faça um programa que leia 5 números e informe o maior número.

"""
maior  = float('-inf')
menor = float('inf')
for i in range(5):
    n = int(input(f'Digite o{i+1}º numero: '))
    maior = n
    menor = n

    if maior < n:
        maior = n 
    if menor > n:
        menor = n     
print(f'\n o maior número digitado foi {maior} ')
print(f'o menor número digitado foi {menor} ')
       
