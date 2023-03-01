print(100*'\033[34m¨\033[m')
n=str(input('\033[34mEscolha +, -, x ou /:\033[m')).strip()
print(100*'\033[34m¨\033[m')
if n=='-':
    pri=float(input('\033[35mDigite um número:\033[m'.strip()))
    se=float(input('\033[35mDigite outro número:\033[m'.strip()))
    print('\033[7:30mSeu resultaddo é:{:.2f}\033[m'.format(pri-se))
if n=='+':
    pr=float(input('\033[33mDigite um número:\033[m'.strip()))
    seg=float(input('\033[33mDigite outro número:\033[m'.strip()))
    print('\033[7:30mSeu resultado é:{:.2f}\033[m'.format(pr+seg))
if n=='x':
    n=float(input('\033[34mDigite um número:\033[m'.strip()))
    s=float(input('\033[34mDigite outro número:\033[m'.strip()))
    print('\033[7:30mSeu resultado é:{:.2f}\033[m'.format(n*s))
if n== '/':
    num=float(input('\033[33mDigite um número:\033[m'.strip()))
    segundo=float(input('\033[33mDigite outro número:\033[m'.strip()))
    print('\033[7:30mSeu resultado é:{:.2f}\033[m'.format(num/segundo))
elif n!='-' or '+' or 'x' or '/':
    print('\033[7mPor favor, reinicie o programa\033[m')