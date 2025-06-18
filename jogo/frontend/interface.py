import tkinter as tk
from tkinter import messagebox
from frontend.jogador import Jogador
from cartas.comprar import comprar_carta
from services.database import Database

class JogoInterface:

    def __init__(self, root, nomes_jogadores):
        self.root = root
        self.root.title("Jogo de Cartas - PvP")
        self.db = Database()
        self.jogadores = [Jogador(nome) for nome in nomes_jogadores]
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

            if raio > 0:
              jogador.turnos_extras += raio
              print(f"{jogador.nome} jogará mais {raio} vez(es) após este turno.")



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

        if raio > 0:
              jogador.turnos_extras += raio
              print(f"{jogador.nome} jogará mais {raio} vez(es) após este turno.")

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
            vencedor = vivos[0]
            self.label_info.config(text=f"{vencedor.nome} venceu!")
            self.botao_avancar.config(state=tk.DISABLED)
            cartas_restantes = len(vencedor.mao)
            self.db.registrar_vitoria(vencedor.nome, vencedor.vida, cartas_restantes)
            self.mostrar_ranking()
            return True
        return False

    def mostrar_ranking(self):
        ranking = self.db.obter_ranking()
        
        ranking_window = tk.Toplevel(self.root)
        ranking_window.title("Ranking de Jogadores")
        
        tk.Label(ranking_window, text="Top 10 Jogadores", font=("Arial", 16)).pack(pady=10)

        frame_header = tk.Frame(ranking_window)
        frame_header.pack(fill=tk.X)
        tk.Label(frame_header, text="Posição", width=10, anchor="w", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        tk.Label(frame_header, text="Jogador", width=20, anchor="w", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        tk.Label(frame_header, text="Vitórias", width=10, anchor="w", font=("Arial", 10, "bold")).pack(side=tk.LEFT)

        for i, (nome, vitorias, ultima_vitoria) in enumerate(ranking, 1):
            frame = tk.Frame(ranking_window)
            frame.pack(fill=tk.X)
            tk.Label(frame, text=f"{i}º", width=10, anchor="w").pack(side=tk.LEFT)
            tk.Label(frame, text=nome, width=20, anchor="w").pack(side=tk.LEFT)
            tk.Label(frame, text=vitorias, width=10, anchor="w").pack(side=tk.LEFT)
        
        tk.Button(ranking_window, text="Fechar", command=ranking_window.destroy).pack(pady=10)