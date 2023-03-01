sa=float(input('qual é o salario do funcionario? R$'))
if sa<=1250:
    novo=sa+(sa*15/100)
else:
    novo=sa+(sa*10/100)
print('quem ganhava R${} passa a ganhar R${:.2f}'.format(sa,novo))