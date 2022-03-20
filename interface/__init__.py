def leiaInt(msg):
    n = ''
    ok = False
    while not ok:
        try:
            n = str(input(f'{msg}'))
            n = int(n)
            ok = True
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return n


def linha(tam=42):
    print('-' * tam)


def cabecalho(txt):
    linha()
    print(f'{txt:^42}')
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for i, v in enumerate(lista):
        print(f'\033[34m{i+1}\033[m - \033[33m{v}\033[m')
    opc = leiaInt('\033[32mSua opção -> \033[m')
    return opc