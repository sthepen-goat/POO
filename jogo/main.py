import tkinter as tk
from tkinter import simpledialog
from frontend.interface import JogoInterface
from frontend.menu_inicial import MenuInicial

def iniciar_jogo(nomes_jogadores):
    app = JogoInterface(root, nomes_jogadores)
    
    def on_closing():
        app.db.fechar_conexao()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)

if __name__ == "__main__":
    root = tk.Tk()
    menu = MenuInicial(root, iniciar_jogo)
    root.mainloop()
    root.withdraw()
    
    num_jogadores = 4
    nomes_jogadores = []
    
    for i in range(num_jogadores):
        nome = simpledialog.askstring(
            "Nome do Jogador", 
            f"Digite o nome do Jogador {i+1}:",
            parent=root
        )
        nomes_jogadores.append(nome if nome else f"Jogador {i+1}")
    
    root.deiconify()
    app = JogoInterface(root, nomes_jogadores)
    
    def on_closing():
        app.db.fechar_conexao()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()