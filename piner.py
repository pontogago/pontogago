
''' esse codigo faz o mouse movimentar e rolar paginas com pausas
    quando usado na pagina do pintrest, faz seu tempo de atividade aumentar
    e por consquencia aumenta suas vizualizações de  forma sutil
'''
import pyautogui
import time
import random

def move_mouse_randomly():
    screen_width, screen_height = pyautogui.size()
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    pyautogui.moveTo(x, y, duration=1)

def main():
    while True:
        # Rolar a página
        pyautogui.scroll(-1000)
        time.sleep(2)
        pyautogui.scroll(-1000)
        time.sleep(2)

        # Mover o mouse aleatoriamente
        move_mouse_randomly()
        time.sleep(1)
        pyautogui.scroll(-1000)
        time.sleep(1)

        move_mouse_randomly()
        time.sleep(1)
        move_mouse_randomly()
        time.sleep(1)

        # Rolar a página novamente
        pyautogui.scroll(-10)
        time.sleep(10)

if __name__ == "__main__":
    main()
