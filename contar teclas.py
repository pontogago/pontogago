import tkinter as tk
from pynput import keyboard

# Função para atualizar a contagem de teclas
def update_key_count(key):
    key = str(key)
    if key in key_counts:
        key_counts[key] += 1
    else:
        key_counts[key] = 1
    text.delete('1.0', tk.END)  # Limpa o texto na janela
    for k, v in key_counts.items():
        text.insert(tk.END, f"{k}: {v}\n")

# Função para monitorar as teclas pressionadas
def on_key_press(key):
    try:
        update_key_count(key.char)
    except AttributeError:
        update_key_count(key)

# Função para salvar a contagem das teclas em um arquivo de texto
def save_key_counts_to_file():
    with open("key_counts.txt", "w") as file:
        for k, v in key_counts.items():
            file.write(f"{k}: {v}\n")

# Inicialização
key_counts = {}
root = tk.Tk()
root.title("Contador de Teclas")

text = tk.Text(root)
text.pack()

# Configuração do monitor de teclado
keyboard_listener = keyboard.Listener(on_press=on_key_press)
keyboard_listener.start()

# Função para fechar o programa
def close_program():
    save_key_counts_to_file()
    root.destroy()
    keyboard_listener.stop()

# Botão para fechar o programa
close_button = tk.Button(root, text="Fechar", command=close_program)
close_button.pack()

root.mainloop()
