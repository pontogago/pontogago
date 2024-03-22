import cv2
import numpy as np
import pygame

# Configuração da câmera
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Configuração da janela
pygame.init()
screen = pygame.display.set_mode((1280, 720))

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

    # Calcula a magnitude do gradiente para encontrar a direção do gradiente
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    magnitude = cv2.magnitude(sobelx, sobely)
    direction = cv2.phase(sobelx, sobely, angleInDegrees=True)

    # Cria uma máscara para selecionar apenas os pixels com valores acima do limite na direção do gradiente
    mask = cv2.inRange(direction, 30, 150)

    # Cria uma imagem com apenas a linha de foco em vermelho
    red_line = np.zeros_like(frame)
    red_line[mask > 0] = (0, 0, 255)
    red_line = cv2.bitwise_and(frame, red_line)

    # Combina a imagem original com a linha de foco em vermelho
    result = cv2.addWeighted(frame, 0.7, red_line, 0.3, 0)

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
