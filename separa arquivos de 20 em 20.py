import os
import shutil

# Diretório de origem onde estão os arquivos a serem separados
diretorio_origem = r'C:\Users\adcp church\Desktop\ebpnl videos'

# Diretório de destino onde os grupos de 20 arquivos serão criados
diretorio_destino = r'C:\Users\adcp church\Desktop\separados'

# Listar os arquivos no diretório de origem
arquivos = os.listdir(diretorio_origem)

# Número de arquivos por grupo
arquivos_por_grupo = 20

# Contador para controlar o número de arquivos em cada grupo
contador = 0

# Variável para criar diretórios de destino separados para cada grupo
grupo = 1

# Loop pelos arquivos e movendo-os para os grupos
for arquivo in arquivos:
    # Construir o caminho completo do arquivo de origem
    caminho_origem = os.path.join(diretorio_origem, arquivo)
    
    # Construir o caminho completo do arquivo de destino
    caminho_destino = os.path.join(diretorio_destino, f'grupo_{grupo}')
    
    # Verificar se o diretório de destino para o grupo atual existe
    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)
    
    # Mover o arquivo para o diretório de destino
    shutil.move(caminho_origem, caminho_destino)
    
    # Incrementar o contador
    contador += 1
    
    # Se o contador atingir o número de arquivos por grupo, reiniciar o contador e passar para o próximo grupo
    if contador == arquivos_por_grupo:
        contador = 0
        grupo += 1

print("Arquivos separados em grupos de 20.")
