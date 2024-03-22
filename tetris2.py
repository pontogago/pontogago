import random
import time

# Lista de peças Tetris

poslinha = [ ## linha 
    [['[]'],
     ['[]'],
     ['[]'],
     ['[]']],
    
    [['[]','[]','[]','[]']] ]

posquadrado = [ ## quadrado
    [['[]','[]'],
     ['[]','[]']]    ]

poslinv = [  ## L invertido
    [['[]','  ','  '],
     ['[]', '[]','[]']],
    
    [['[]','[]'],
     ['[]','  '],
     ['[]','  ']],
    
    [['[]','[]','[]'],
     ['  ','  ','[]']],

    [['  ','[]'],
     ['  ','[]'],
     ['[]','[]']]    ]

posl = [ ## L normaç
    [['  ','  ','[]'],
     ['[]','[]','[]']],

    [['[]','  '],
     ['[]','  '],
     ['[]','[]']],

    [['[]', '[]','[]'],
     ['[]', '  ','  ']],

    [['[]','[]'],
     ['  ','[]'],
     ['  ','[]']]    ]

poszigzag = [ ## zig zag
    [['[]','[]','  '],
     ['  ','[]','[]']],
    
    [['  ','[]'],
     ['[]','[]'],
     ['[]','  ']]    ]

poszigzaginv = [  ## zig zag invertido
    [['  ','[]','[]'],
     ['[]','[]','  ']],
    
    [['[]','  '],
     ['[]','[]'],
     ['  ','[]']]  ]

postreta = [  ## treta T
    [['[]','[]','[]'],
     ['  ','[]','  ']],
    
    [['  ','[]'],
     ['[]','[]'],
     ['  ','[]']],
    
    [['  ','[]','  '],
     ['[]','[]','[]']],
    
    [['[]','  '],
     ['[]','[]'],
     ['[]','  ']]  ]


def imprimir(peca):
    for linha in peca:
        for segmento in linha:
            print(segmento, end='')
        print()
    

#imprimir(poslinha[0]) # teste de qual peça especifca

    
def pecaatual():
    intervalo = random.randint(1, 7)
    intervalolinha = random.randint(0, 1)
    intervalol = random.randint(0, 3)
    intervalolinv = random.randint(0, 3)
    intervalozigzag = random.randint(0, 1)
    intervalozigzaginv = random.randint(0, 1)
    intervalotreta = random.randint(0, 3)
    
    if intervalo == 1:
        return poslinha[(intervalolinha)]
    elif intervalo == 2:
        return posquadrado[0]
    elif intervalo == 3:
        return posl[(intervalol)]
    elif intervalo == 4:
        return poslinv[(intervalolinv)]
    elif intervalo == 5:
        return poszigzag[(intervalozigzag)]
    elif intervalo == 6:
        return poszigzaginv[(intervalozigzaginv)]
    elif intervalo == 7:
        return postreta[(intervalotreta)]



campolarg = 10
campoaltu = 20

def imprimircampo(campo):
    for linha in campo:
        print(linha)

def criarcampo():
    return [[' ' for i in range(campolarg)] for i in range(campoaltu)]

def adicionarpeca(campo, peca, x, y):
    for i, linha in enumerate(peca):
        for j, segmento in enumerate(linha):
            if segmento == '[]':
                campo[y + i][x + j] = segmento


def podecolocar (campo, peza, x, y):
    for i, linha in enumerate(peza):
        for j, segmento in enumerate(linha):
            if segmento == '[]':
                if(y + i >= campoaltu or x + j < 0 or x + j >= campolarg or campo [y+i][x + j] != ' ' ):
                    return False

    return True

def remover_linhas_completas(campo):
    linhas_completas = [i for i, linha in enumerate(campo) if '  ' not in linha]
    for linha_completa in linhas_completas:
        del campo[linha_completa]
        campo.insert(0, ['  '] * campolarg)

campodejogo = criarcampo()
   
x_pecatual = campolarg // 2 - 1
y_pecatual = 0

delay = 0.1  # Ajuste o valor deste atraso (em segundos) conforme desejado

while True:

    import os

    os.system('cls' if os.name == 'nt' else 'clear')

    if podecolocar(campodejogo, pecaatual(), x_pecatual, y_pecatual + 1):
        y_pecatual += 1
        time.sleep(delay)  # Adicione um atraso após cada movimento
    else:

        adicionarpeca(campodejogo, pecaatual(), x_pecatual, y_pecatual)
        remover_linhas_completas(campodejogo)

        pecaatual()
        x_pecatual = campolarg // 2 - 1
        y_pecatual = 0


    imprimircampo(campodejogo)
