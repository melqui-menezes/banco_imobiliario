from entidade.tabuleiro import Tabuleiro

class Partida:
    
    def __init__(self):
        self.vencedor = None
        self.timeout = False
        self.rodada = 0
        self.tabuleiro = Tabuleiro()
    
    def iniciar_rodada(self,jogadores:list):
        for jogador in jogadores:
            if jogador.saldo_positivo():
                posicao_propriedade = self.tabuleiro.jogar_dado(jogador)
                propriedade = self.tabuleiro.propriedades[posicao_propriedade]
                if not propriedade.nome == 'Início':
                    jogador.decidir_acao(propriedade)
            else:
                self.tabuleiro.excluir_jogador(jogador)
    
    def iniciar_partida(self):
        while not self.timeout and len(self.tabuleiro.jogadores) > 1:
            self.iniciar_rodada(self.tabuleiro.jogadores)
            self.rodada += 1
            self.timeout = True if self.rodada == 1000 else False
        if self.timeout:
            self.vencedor = self.tabuleiro.verifica_vencedor()
        else:
            self.vencedor = self.tabuleiro.jogadores[0]
        
        