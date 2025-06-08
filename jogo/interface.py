import tkinter as tk
from jogador import Jogador
from cartas.comprar import comprar_carta

class JogoInterface:
    def __init__(self, root, num_jogadores=4):
        self.root = root
        self.root.title("Jogo de Cartas - PvP")
        self.jogadores = [Jogador(f"Jogador {i+1}") for i in range(num_jogadores)]
        for j in self.jogadores:
            j.jogo = self
            j.turnos_extras = 0  
        self.indice_turno = 0
        self.carta_pendente = None

        self.label_info = tk.Label(root, text="", font=("Arial", 14))
        self.label_info.pack()

        self.frame_mao = tk.Frame(root)
        self.frame_mao.pack()

        self.frame_alvos = tk.Frame(root)
        self.frame_alvos.pack()

        self.botao_avancar = tk.Button(root, text="Pular Turno (sem ação)", command=self.pular_turno)
        self.botao_avancar.pack()

        self.atualizar_interface()

    def atualizar_interface(self):
        jogador = self.jogadores[self.indice_turno]
        self.label_info.config(text=f"Turno de {jogador.nome} | Vida: {jogador.vida}")

        for widget in self.frame_mao.winfo_children():
            widget.destroy()
        for widget in self.frame_alvos.winfo_children():
            widget.destroy()

        if jogador.estado == "silenciado":
            print(f"{jogador.nome} está silenciado e não pode jogar neste turno.")
            jogador.estado = None
            jogador.comprar()
            self.proximo_turno()
            return

        for i, carta in enumerate(jogador.mao):
            btn = tk.Button(
                self.frame_mao,
                text=f"{carta.nome}\n({carta.descricao})",
                command=lambda i=i: self.jogar_carta(i),
                width=20,
                height=6,
                wraplength=140,
                font=("Arial", 10)
            )
            btn.pack(side=tk.LEFT, padx=5)

    def jogar_carta(self, indice):
        jogador = self.jogadores[self.indice_turno]
        carta = jogador.mao.pop(indice)
        jogador.ultima_carta = carta

        precisa_de_alvo = getattr(carta, "precisa_alvo", False)
        raio = getattr(carta, "raio", 0)  

        if precisa_de_alvo:
            self.carta_pendente = carta
            self.exibir_opcoes_de_alvo()
        else:
            if hasattr(carta, "aplicar_efeito"):
                carta.aplicar_efeito(jogador, jogador)

            if raio == 1:
                jogador.turnos_extras += raio - 1
                print(f"{jogador.nome} ganhou {raio - 1} turnos extras!")
            
            if raio == 2:
                jogador.turnos_extras += raio -2
                

            jogador.comprar()
            self.proximo_turno()

    def exibir_opcoes_de_alvo(self):
        for widget in self.frame_alvos.winfo_children():
            widget.destroy()

        for i, jogador in enumerate(self.jogadores):
            if i != self.indice_turno and jogador.vida > 0:
                btn = tk.Button(
                    self.frame_alvos,
                    text=f"{jogador.nome} ({jogador.vida} vida)",
                    command=lambda i=i: self.atacar_jogador(i)
                )
                btn.pack(side=tk.LEFT, padx=5)

    def atacar_jogador(self, indice_alvo):
        carta = self.carta_pendente
        jogador = self.jogadores[self.indice_turno]
        alvo = self.jogadores[indice_alvo]

        raio = getattr(carta, "raio", 0)

        if hasattr(carta, "aplicar_efeito"):
            carta.aplicar_efeito(jogador, alvo)
        elif hasattr(carta, "dano"):
            alvo.vida -= carta.dano
            if alvo.vida < 0:
                alvo.vida = 0

        if raio > 1:
            jogador.turnos_extras += raio - 1
            print(f"{jogador.nome} ganhou {raio - 1} turnos extras!")

        self.carta_pendente = None
        jogador.comprar()
        self.proximo_turno()

    def pular_turno(self):
        self.jogadores[self.indice_turno].comprar()
        self.proximo_turno()

    def proximo_turno(self):
        if self.verificar_fim_de_jogo():
            return

        jogador = self.jogadores[self.indice_turno]

        if jogador.turnos_extras > 0:
            jogador.turnos_extras -= 1
            self.atualizar_interface()
            return

        total = len(self.jogadores)
        for _ in range(total):
            self.indice_turno = (self.indice_turno + 1) % total
            jogador = self.jogadores[self.indice_turno]
            if jogador.vida > 0:
                break

        self.atualizar_interface()

    def verificar_fim_de_jogo(self):
        vivos = [j for j in self.jogadores if j.vida > 0]
        if len(vivos) == 1:
            self.label_info.config(text=f"{vivos[0].nome} venceu!")
            self.botao_avancar.config(state=tk.DISABLED)
            return True
        return False
