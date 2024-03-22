'''
import random
import matplotlib.pyplot as plt

def simulacao_roleta(total_partidas):
    resultados = []
    contagem_vermelho = 0
    contagem_preto = 0

    for _ in range(total_partidas):
        resultado = 'vermelho' if random.random() < 0.5 else 'preto'

        if resultado == 'vermelho':
            contagem_vermelho += 1
        else:
            contagem_preto += 1

        resultados.append(resultado)

    return resultados, contagem_vermelho, contagem_preto

def plotar_grafico_roleta(resultados, contagem_vermelho, contagem_preto):
    x = list(range(1, len(resultados)+1))
    y_vermelho = [contagem_vermelho] * len(resultados)
    y_preto = [contagem_preto] * len(resultados)

    plt.plot(x, ["veremlho" if resultado == 'vermelho' else "preto" for resultado in resultados], color='green')

    plt.xlabel(f'{contagem_vermelho} vermelho')
    plt.title(f'{contagem_preto} preto')
    plt.show()

def main():
    total_partidas = 100

    resultados, contagem_vermelho, contagem_preto = simulacao_roleta(total_partidas)
    plotar_grafico_roleta(resultados, contagem_vermelho, contagem_preto)

if __name__ == "__main__":
    main()
'''

import random
import matplotlib.pyplot as plt

def simulacao_roleta(total_partidas):
    resultados = []
    contagem_vermelho = 0
    contagem_preto = 0
    contagem_verde = 0

    probabilidade_verde = 2/38  # Ajuste para equilibrar as probabilidades

    for _ in range(total_partidas):
        if random.random() < probabilidade_verde:
            resultado = 'verde'
            contagem_verde += 1
        else:
            resultado = 'vermelho' if random.random() < 0.5 else 'preto'
            if resultado == 'vermelho':
                contagem_vermelho += 1
            else:
                contagem_preto += 1

        resultados.append(resultado)

    return resultados, contagem_vermelho, contagem_preto, contagem_verde


def plotar_grafico_roleta(resultados, contagem_vermelho, contagem_preto, contagem_verde):
    x = list(range(1, len(resultados)+1))
    y_vermelho = [contagem_vermelho] * len(resultados)
    y_preto = [contagem_preto] * len(resultados)
    y_verde = [contagem_verde] * len(resultados)

    cores = ["vermelho" if resultado == 'vermelho' else ("preto" if resultado == 'preto' else 'verde') for resultado in resultados]

    plt.plot(x, cores, color='green')

    plt.xlabel(f'{contagem_vermelho} vermelho, {contagem_preto} preto, {contagem_verde} verde')
  ##  plt.title('Roleta de Cassino')
    plt.show()

def tabela_aposta():
    print("Tabela de Aposta:")
    print("  - Número Par: Pagamento 2:1")
    print("  - Número Ímpar: Pagamento 2:1")
    print("  - Vermelho: Pagamento 2:1")
    print("  - Preto: Pagamento 2:1")
    print("  - Verde: Pagamento 17:1 (zero)")





def main():
    total_partidas = 100

    resultados, contagem_vermelho, contagem_preto, contagem_verde = simulacao_roleta(total_partidas)
    plotar_grafico_roleta(resultados, contagem_vermelho, contagem_preto, contagem_verde)
    tabela_aposta()

if __name__ == "__main__":
    main()
