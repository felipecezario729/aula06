"""

Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
# len >> função que retorna o tamanha do campo valor informado
while True:
    nome = input('digite um nome ')
    idade = input('digite sua idade')
    salario = int(input('digite seu salario '))
    sexo = int(input('digite seu sexo {f} feminino {M} masculino'))
    estado_civil = 's','c', 'v', 'd'

"""
nome = input('digite o nome')
while len(nome)<3:
    nome = input('Digite o nome')
    print(f'Digitou um nome menor que 3 =<{nome}')
idade = int(input('digite sua idade [0 - 150]'))
while idade  < 0 or idade > 150:
   idade = int(input('digite sua idade [0 - 150]'))
   print('Você digitou a idade errada')
else:
    print('voce digitou um valor valido')
salario = float(input('digite seu Salario'))
if salario > 0:
   print(f'digite o valor do salario')
else:
    print('digite seu salario')     
