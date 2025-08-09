"""
Supondo que a população de um país A seja da ordem de 80000 
habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000
 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva
 o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

"""
população1 = 80000
população2 = 200000
# valor da taxa em percentual 
taxa1 = 0.03
taxa2 = 0.015
ano = 0
while população1 < população2:
    população1 += população1 * taxa1
    população2 +=  população2 * taxa2
    ano += 1
    print(f'Ano {ano}: população1 a ={int(população1)}, população2 b = {int(população2)}')
print(f'A população a ultrapassou ou igualou b em {ano}')
