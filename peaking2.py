import cv2
import numpy as np
import pygame

# Configuração da câmera
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

# Configuração da janela
pygame.init()
screen = pygame.display.set_mode((720, 500))

while True:
    # Captura a imagem da câmera
    ret, frame = cap.read()
    if not ret:
        continue

    # Converte a imagem para tons de cinza e aplica uma gaussiana para suavizar
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Calcula o laplaciano da imagem para encontrar as bordas
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    # Aplica uma função de transferência para destacar as bordas em vermelho
    transfer = np.zeros_like(laplacian)
    transfer[laplacian > 1] = 255
    transfer = cv2.cvtColor(transfer.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    transfer[:,:,1:] = 0

    # Combina a imagem original com as bordas destacadas em vermelho
    result = cv2.addWeighted(frame, 0.7, transfer, 0.3, 0)

    # Inverte a imagem horizontalmente
    result = cv2.flip(result, 1)

    # Exibe a imagem na janela
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    result = np.rot90(result)
    result = pygame.surfarray.make_surface(result)
    screen.blit(result, (0, 0))
    pygame.display.flip()

    # Verifica se o usuário pressionou a tecla Esc para sair
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            cap.release()
            cv2.destroyAllWindows()
            pygame.quit()
            quit()
