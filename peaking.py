import cv2
import numpy as np

# Abre a câmera USB
cap = cv2.VideoCapture(1)

# Define os parâmetros do algoritmo de focus peaking
sigma = 10
thresh = 50

while(True):
    # Captura um frame da câmera
    ret, frame = cap.read()
    
    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calcula o gradiente da imagem usando um filtro gaussiano
    grad = cv2.GaussianBlur(gray, (0, 0), sigma) - cv2.GaussianBlur(gray, (0, 0), sigma*2)
    
    # Aplica uma limiarização para destacar as áreas mais nítidas
    bw = cv2.threshold(grad, thresh, 300, cv2.THRESH_BINARY)[1]
    
    # Aplica um filtro morfológico para remover ruídos
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
    bw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    
    # Converte a imagem de volta para BGR para exibir o resultado
    bw_bgr = cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)
    
    # Exibe o resultado em uma janela
    cv2.imshow('Focus Peaking', cv2.addWeighted(frame, 1.9, bw_bgr, 1.9, 0))
    
    # Aguarda pela tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha a janela
cap.release()
cv2.destroyAllWindows()
