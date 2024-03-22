import tkinter as tk
import pyautogui

def atualizar_coordenadas():
    x, y = pyautogui.position()
    coordenadas_label.config(text=f'X={x+1}, Y={y+1}')
    coordenadas_label.after(10, atualizar_coordenadas)  # Atualiza a cada 100 milissegundos

app = tk.Tk()
app.title('')
app.geometry('100x25')

coordenadas_label = tk.Label(app, text='', font=('Helvetica', 10))
coordenadas_label.pack(pady=00)

atualizar_coordenadas()

app.mainloop()
