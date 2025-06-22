from cartas.comprar import comprar_carta

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 10
        self.mao = [comprar_carta() for _ in range(7)]
        self.estado = None
        self.ultima_carta = None
        self.turnos_extras = 0
    
    def comprar(self):
        nova_carta = comprar_carta()
        self.mao.append(nova_carta)
        print(f"{self.nome} comprou a carta: {nova_carta.nome}")
