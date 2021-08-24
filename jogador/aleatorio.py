from jogador.jogador_base import JogadorBase

import random


class Aleatorio(JogadorBase):
    
    def __init__(self, name):
        return  super().__init__(name)
    
    def decidir_acao(self, propriedade):
        if propriedade.proprietario:
            propriedade.pagar_aluguel(self)
        else:    
            decisao = random.choice(['sim','não'])
            if decisao == 'sim':
                propriedade.comprar(self)