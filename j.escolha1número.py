from random import randint
com=randint(0,5)
di=int(input('escolha um número entre 0 e 5:'))
print('processando...')
if di==com:
    print('parabens! você ganhou!')
else:
    print('ops, você perdeu!')