r=float(input('primeironlado do triangulo:'))
rb=float(input('segundo lado:'))
rc=float(input('terceiro lado:'))
if r < rb + rc and rb < r + rc and rc < r + rb:
    print('\033[4:34:40messes valores podem formar um \033[0:32mtriangulo!')
else:
    print('esses valores nao podem formar um triangulo')