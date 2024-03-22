'''
import random

def simular_cara_coroa(porcentagem, num_partidas):
    # Inicializa o contador de caras e coroas
    caras = 0
    coroas = 0

    # Loop para simular as partidas
    for _ in range(num_partidas):
        # Gera um número aleatório entre 0 e 1
        resultado = random.uniform(0, 1)

        # Compara com a porcentagem para determinar cara ou coroa
        if resultado < porcentagem:
            caras += 1
        else:
            coroas += 1

    # Exibe os resultados
    print(f"Simulação concluída em {num_partidas} partidas.")
    print(f"Número de caras: {caras}")
    print(f"Número de coroas: {coroas}")
    print(f"Porcentagem de caras: {caras / num_partidas * 100:.2f}%")
    print(f"Porcentagem de coroas: {coroas / num_partidas * 100:.2f}%")

# Defina a porcentagem desejada
porcentagem_cara = 0.6  # 50%

# Número total de partidas a serem simuladas
num_partidas_simuladas = 10000

# Chama a função de simulação
simular_cara_coroa(porcentagem_cara, num_partidas_simuladas)

'''
import random
import matplotlib.pyplot as plt

def simulacao_cara_coroa(porcentagem_cara, total_partidas):
    resultados = []
    contagem_cara = 0
    contagem_coroa = 0

    for _ in range(total_partidas):
        ##resultado = 'cara' if random.random() < porcentagem_cara else 'coroa'
        resultado = 'cara' if random.random() < porcentagem_cara else 'coroa'

        if resultado == 'cara':
            contagem_cara += 1
        else:
            contagem_coroa += 1

        resultados.append(resultado)

    return resultados, contagem_cara, contagem_coroa

def plotar_grafico(resultados, contagem_cara, contagem_coroa):
    x = list(range(1, len(resultados)+1))
    y_cara = [contagem_cara] * len(resultados)
    y_coroa = [contagem_coroa] * len(resultados)

    plt.plot(x, ["cara" if resultado == 'cara' else "coroa" for resultado in resultados], color='red')

    plt.xlabel(f'{contagem_cara} caras')
    plt.title(f'{contagem_coroa} coroas')
    
    plt.show()

def main():
    porcentagem_cara = 0.6  # Porcentagem de chance de sair cara
    total_partidas = 1000

    resultados, contagem_cara, contagem_coroa = simulacao_cara_coroa(porcentagem_cara, total_partidas)
    plotar_grafico(resultados, contagem_cara, contagem_coroa)

if __name__ == "__main__":
    main()


    
