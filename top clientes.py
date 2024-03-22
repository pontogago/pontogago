from collections import Counter

# Lê o arquivo de entrada
with open('nomes do crientes.txt', 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

# Conta a ocorrência de cada linha
contador = Counter(linhas)

# Organiza as contagens do maior para o menor
contagens_ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)

# Cria um arquivo de saída com as contagens organizadas
with open('contagem_linhas_ordenadas.txt', 'w') as arquivo_saida:
    for linha, quantidade in contagens_ordenadas:
        arquivo_saida.write(f'{linha.strip()}: {quantidade}\n')

print('Contagem de linhas concluída e organizada. Resultados salvos em contagem_linhas_ordenadas.txt')
