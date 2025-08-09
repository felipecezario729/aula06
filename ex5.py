"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
 Valide a entrada e permita repetir a operação.
"""
população1 = float(input('Digite a população de a '))
população2 = float(input('Digite a população de B'))
# valor da taxa em percentual 
taxa1 = float(input('Digite a taxa de crescimento A '))
taxa1 = taxa1 / 100
taxa2 = float(input('digite a taxa de crescimento B'))
taxa2 = taxa2 / 100
ano = 0

while população1 < população2:
    população1 += população1 * taxa1
    população2 +=  população2 * taxa2
    ano += 1
    print(f'Ano {ano}: população1 a ={int(população1)}, população2 b = {int(população2)}')
print(f'A população a ultrapassou ou igualou b em {ano}')