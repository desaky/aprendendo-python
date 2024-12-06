# exercício para o computador escolher um número entre 0 e 5 e o usuário tentar adivinhar

import random
nc = random.randint(0, 5)
nu = int(input('Qual número você acha que vai ser sorteado?: '))
if nc == nu:
    print('Você acertou! o número era {}'.format(nc))
else :
    print('Você errou! o numero era {}'.format(nc))