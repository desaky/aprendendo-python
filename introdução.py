#PRIMEIROS CÓDIGOS EM PYTHON

# Alguns códigos básicos: 

nome = input('Qual o seu nome? \n')

print('É um praze te conhecer, {}!'.format(nome))

# Tipos primitivos e saída de dados:

# n1 = int(input('Digite um número: '))

# n2 = int(input('Digite mais um número:'))

# s = (n1) + (n2)

# print('A soma dos números {} e {} é: {}'.format(n1, n2, s))

# Tipos de números mais usados:

# int // float // bool // str

n = str(input('Digite um valor: \n'))

print(n.isnumeric())

# Aqui vemos como pegar todas as informações de uma variável:

a = input('Digite algo: \n')
print('O tipo primitivo desse valor é ' , type(a))
print('Só tem espaços? ' , a.isspace())
print('É um número? ' , a.isnumeric())
print('É alfabético? ' , a.isalpha())
print('é alfanumérico? ' , a.isalnum())
print('Está em maiúscula? ' , a.isupper())
print('Está em minúscula? ' , a.islower())
print('Está capitalizado? ' , a.istitle())

# exercícios de pyton

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))