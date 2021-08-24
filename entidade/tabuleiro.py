from random import randint, sample

from entidade.propriedade import Propriedade
from jogador.aleatorio import Aleatorio
from jogador.cauteloso import Cauteloso
from jogador.exigente import Exigente
from jogador.impulsivo import Impulsivo

class Tabuleiro:
    
    def __init__(self):
        self.propriedades = [
            Propriedade("Início",0),
            Propriedade("Rua Tiradentes",130),
            Propriedade("Rua Alagoas",150),
            Propriedade("Rua Sergipe",150),
            Propriedade("Rua Bahia",200),
            Propriedade("Rua Amazonas",185),
            Propriedade("Rua Dezoito",175),
            Propriedade("Rua Sao Sebastiao",155),
            Propriedade("Rua Parana",90),
            Propriedade("Rua Bela Vista",130),
            Propriedade("Rua Santa Luzia",190),
            Propriedade("Rua Sao Jorge",100),
            Propriedade("Rua Parque das Pedras",85),
            Propriedade("Rua Castro Alves",85),
            Propriedade("Rua Duque De Caxias",75),
            Propriedade("Rua Projetada",130),
            Propriedade("Rua Rui Barbosa",105),
            Propriedade("Rua Santa Catarina",95),
            Propriedade("Rua Minas Gerais",90),
            Propriedade("Rua Santos Dumont",145),
            Propriedade("Rua Espirito Santo",60),
        ]
        self.jogadores = sample(
            [
                Impulsivo('Impulsivo'),
                Exigente('Exigente'),
                Cauteloso('Cauteloso'),
                Aleatorio('Aleatório')
            ]
        ,4)
    
    def jogar_dado(self, jogador):
        dado = randint(1,6)
        nova_posicao = jogador.avancar_posicao(dado)
        return nova_posicao
        
    def remover_propriedades(self, jogador):
        for propriedade in self.propriedades:
            if propriedade.proprietario == jogador:
                propriedade.proprietario = None

    def excluir_jogador(self,jogador):
        self.remover_propriedades(jogador)
        self.jogadores.remove(jogador)
    
    def verifica_vencedor(self):
        maior_saldo = 0
        for jogador in self.jogadores:
            if jogador.saldo > maior_saldo:
                vencedor = jogador
                maior_saldo = jogador.saldo
        return vencedor