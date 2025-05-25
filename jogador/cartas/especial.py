import random
from cartas import Carta

class CartaEspecial(Carta):
    def __init__(self):
        self.efeito = random.choice([ "silenciar", "espelhar", "embaralhar"])
        descricao = {
            "silenciar": "Impede o alvo de jogar carta no próximo turno.",
            "espelhar": "Copia o efeito da última carta jogada pelo alvo.",
            "embaralhar": "Troca todas as cartas do alvo por novas cartas."
        }[self.efeito]

        super().__init__("Carta Especial", descricao)
        self.precisa_alvo = True


    def aplicar_efeito(self, jogador, oponente):
        if self.efeito == "silenciar":
            oponente.estado = "silenciado"
            print(f"{oponente.nome} foi silenciado e não poderá usar cartas no próximo turno.")
        elif self.efeito == "espelhar":
            if hasattr(oponente, 'ultima_carta'):
                carta = oponente.ultima_carta
                carta.aplicar_efeito(jogador, oponente)
                print(f"{jogador.nome} espelha o efeito da carta {carta.nome}.")
            else:
                print(f"{jogador.nome} tentou espelhar, mas {oponente.nome} ainda não jogou nenhuma carta.")
        elif self.efeito == "embaralhar":
            oponente.mao.clear()
            for _ in range(7): 
                oponente.comprar()
            print(f"{oponente.nome} teve suas cartas trocadas.")

