from operações import *
from interface import *
from time import sleep

while True:
    esc = menu(['soma', 'subtração', 'multiplicação', 'divisão', 'sair do sistema'])
    if esc == 1:
        cabecalho('SOMA')
        s()
        sleep(2)
    elif esc == 2:
        cabecalho('SUBTRAÇÃO')
        n1 = leiaInt('Primeiro número: ')
        n2 = leiaInt('Segundo número: ')
        sub(n1, n2)
        sleep(2)
    elif esc == 3:
        cabecalho('MULTIPLICAÇÃO')
        mult()
        sleep(2)
    elif esc == 4:
        cabecalho('DIVISÃO')
        n1 = leiaInt('Dividendo: ')
        n2 = leiaInt('Divisor: ')
        div(n1, n2)
        sleep(2)
    elif esc == 5:
        cabecalho('FINALIZANDO...ATÈ LOGO!')
        sleep(1)
        break
    else:
        print('ERRO! Selecione uma opção válida.')
