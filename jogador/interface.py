import tkinter as tk
from jogador import Jogador

class JogoInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Batalha de Cartas PvP")

        self.jogadores = [Jogador("Jogador 1"), Jogador("Jogador 2")]
        self.turno = 0

        self.label_vez = tk.Label(root, text="", font=("Arial", 14))
        self.label_vez.pack(pady=10)

        self.label_vida = tk.Label(root, text="", font=("Arial", 12))
        self.label_vida.pack(pady=10)

        self.quadro_mao = tk.Frame(root)
        self.quadro_mao.pack()

        self.mensagem = tk.Label(root, text="", font=("Arial", 10))
        self.mensagem.pack(pady=5)

        self.atualizar_interface()

    def atualizar_interface(self):
        jogador = self.jogadores[self.turno]
        oponente = self.jogadores[1 - self.turno]

        self.label_vez.config(text=f"Vez de {jogador.nome}")
        self.label_vida.config(text=f"{self.jogadores[0].nome}: {self.jogadores[0].vida} | {self.jogadores[1].nome}: {self.jogadores[1].vida}")
        self.mensagem.config(text="Escolha uma carta para jogar:")

        for widget in self.quadro_mao.winfo_children():
            widget.destroy()

        for i, carta in enumerate(jogador.mao):
            btn = tk.Button(self.quadro_mao, text=f"{carta.nome}\n({carta.descricao})", width=25, height=4,
                            command=lambda i=i: self.jogar_carta(i))
            btn.grid(row=0, column=i, padx=5)

    def jogar_carta(self, indice):
        jogador = self.jogadores[self.turno]
        oponente = self.jogadores[1 - self.turno]

        jogador.usar_carta(indice, oponente)

        if not oponente.esta_vivo():
            self.mensagem.config(text=f"{jogador.nome} venceu!")
            for widget in self.quadro_mao.winfo_children():
                widget.destroy()
            return

        self.turno = 1 - self.turno
        self.atualizar_interface()
