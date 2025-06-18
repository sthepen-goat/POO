import random
from cartas.arma import CartaArma
from cartas.agilidade import CartaAgilidade
from cartas.armadura import CartaArmadura
from cartas.bloqueador import CartaBloqueador
from cartas.especial import CartaEspecial

def comprar_carta():
    opcoes = [
        CartaArma, CartaAgilidade,
        CartaArmadura, CartaBloqueador,
        CartaEspecial
    ]
    return random.choice(opcoes)()