from entidade.partida import Partida


class SimuladorBancoImobiliario:
    
    def __init__(self,qtd_simulacoes:int=None):
        self.qtd_simulacoes = qtd_simulacoes or 300
        self.resultados = []
        self.timeouts = 0
        self.media_rodadas = 0
        self.vitorias_comportamento = {
            "Impulsivo":0,
            "Exigente":0,
            "Cauteloso":0,
            "Aleatório":0,
        }
        self.mais_eficiente = None
        self.simular_partidas()
        self.analise_resultados()

    def simular_partidas(self):
        partida = 0
        while partida < self.qtd_simulacoes:
            jogo = Partida()
            jogo.iniciar_partida()
            self.resultados.append({
                'timeout':jogo.timeout,
                'turnos':jogo.rodada,
                'vencedor': jogo.vencedor.nome
            })
            partida += 1
        
    def analise_resultados(self):
        for partida in self.resultados:
            if partida['timeout']:
                self.timeouts += 1
            self.media_rodadas += partida.get('turnos')
            self.vitorias_comportamento[partida.get('vencedor')] += 1
        mais_vitorias = 0
        for comportamento in self.vitorias_comportamento:
            if self.vitorias_comportamento.get(comportamento) > mais_vitorias:
                mais_vitorias = self.vitorias_comportamento.get(comportamento)
                self.mais_eficiente = comportamento
        self.media_rodadas = self.media_rodadas / self.qtd_simulacoes
    
    def __str__(self):
        return str({
            "Quantidade de timeouts": self.timeouts,
            "Média de turnos por partida": round(self.media_rodadas,2),
            "Comportamento mais vitorioso": self.mais_eficiente,
            "Vitórias por comportamento": self.vitorias_comportamento
        })

    
if __name__ == '__main__':
   print(SimuladorBancoImobiliario())
   