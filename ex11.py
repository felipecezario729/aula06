"""
Altere o programa anterior para mostrar no final a soma dos números.
"""
soma = 0
n1 = int(input('digite o primeiro numero '))
n2 = int(input('digite o segunto numero'))

for i in range(n1+1 , n2):
    print(i, end='')
    soma = soma + i
print(f'A soma dos números digitados é {soma} ')