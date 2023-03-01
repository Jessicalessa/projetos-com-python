na=eval(input('primeiro numero'))
nb=eval(input('segundo numero'))
nc=eval(input('terceiro numero'))
if (na>nb) and (na>nc) and (nb>nc):
    print('o primeiro é o maior')
if (nb>nc) and (nb>na) and (na>nc):
    print('o segundo')
if (nc>na) and (nc>nb) and (na>nb):
    print('terceiro')
print('fim')