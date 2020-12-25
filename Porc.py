from random import randint

opc1 = ''
opc2 = ''

opc1porc = 0
opc2porc = 0

porc = 0

R = 0

opc1 = str(input('Opção 1: '))
opc2 = str(input('Opção 2: '))

porc = int(input('Porcentagem máxima: '))

opc1porc = int(input(f'Porcentagem da opção 1: '))

R = randint(0, porc)

if(R < opc1porc):
    print(f'{opc1}')
else:
    print(f'{opc2}')

print(R)