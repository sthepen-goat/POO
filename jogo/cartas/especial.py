import random
from cartas import Carta

class CartaEspecial(Carta):
    def __init__(self):
        self.efeito = random.choice([
            "silenciar",
            "espelhar",
            "embaralhar",
            "bola_de_fogo",
            "trocar_vida",
        ])

        descricao = {
            "silenciar": "Impede o alvo de jogar carta no próximo turno.",
            "espelhar": "Copia o efeito da última carta jogada pelo alvo.",
            "embaralhar": "Troca todas as cartas do alvo por novas cartas.",
            "bola_de_fogo": "Causa 3 de dano a todos os jogadores.",
            "trocar_vida": "Troca sua vida com a do alvo.",
        }[self.efeito]

        super().__init__("Carta Especial", descricao)
        self.precisa_alvo = self.efeito in ["silenciar", "espelhar", "embaralhar", "trocar_vida"]

    def aplicar_efeito(self, jogador, oponente=None):
        if self.efeito == "silenciar":
            oponente.estado = "silenciado"
            print(f"{oponente.nome} foi silenciado e não poderá usar cartas no próximo turno.")

        elif self.efeito == "espelhar":
            if hasattr(oponente, 'ultima_carta') and oponente.ultima_carta:
                carta = oponente.ultima_carta
                carta.aplicar_efeito(jogador, oponente)
                print(f"{jogador.nome} espelhou o efeito da carta {carta.nome}.")
            else:
                print(f"{jogador.nome} tentou espelhar, mas {oponente.nome} ainda não jogou nenhuma carta.")

        elif self.efeito == "embaralhar":
            oponente.mao.clear()
            for _ in range(7):
                oponente.comprar()
            print(f"{oponente.nome} teve suas cartas trocadas.")

        elif self.efeito == "bola_de_fogo":
            for p in jogador.jogo.jogadores:
                p.vida -= 3
                if p.vida < 0:
                    p.vida = 0
                print(f"{p.nome} recebeu 3 de dano da Bola de Fogo!")

        elif self.efeito == "trocar_vida":
            jogador.vida, oponente.vida = oponente.vida, jogador.vida
            print(f"{jogador.nome} trocou de vida com {oponente.nome}!")
