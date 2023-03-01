nome=str(input('\033[35mQual seu nome?\033[m')).strip()
senha=(input('\033[35mInforme uma senha:\033[m')).upper().strip()
sn=(input('\033[35mVocê está bem?(digite sim ou não)\033[m')).upper().strip()
if sn=='SIM':
    print('\033[7mQue bom que você está bem {}! Se precisar conversar estou aqui!\033[m'.format(nome))
if sn=='NÃO':
    desa=str(input('\033[34mSinto muito! Conte-me tudo o que quiser contar{} {}{}{}:'.format('\033[m','\033[34m',nome,'\033[m'))).strip
elif sn!='SIM' or 'NÂO':
    print('\033[31mEroor\033[m')
dix=desa
pre=(input('\033[34mQuer ver as anotações?(digite sim ou não)\033[m')).upper().strip()
if pre=='SIM':
    sii=(input('\033[4;31mQual a sua senha?\033[m')).upper().strip()
    if sii==senha:
        print(dix)
    if sii !=senha:
        print('\033[7;31;43mDesculpe, senha errada!\033[m')
if pre=='NÂO':
    print('\033[7m\033[35mObrigado, e até a próxima!\033[m')