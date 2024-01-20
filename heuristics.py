def get_heuristic1(self):
    if self.End():
        if self.mancala[13] > self.mancala[6]:
            return 100
        elif self.mancala[13] == self.mancala[6]:
            return 0
        else:
            return -100
    else:
        return self.mancala[13] - self.mancala[6]



def get_heuristic2(self):
    if self.End():
        if self.mancala[13] > self.mancala[6]:
            return 100
        elif self.mancala[13] == self.mancala[6]:
            return 0
        else:
            return -100
    else:
        player_pits = [self.mancala[i] for i in range(0, 6)]
        opponent_pits = [self.mancala[i] for i in range(7, 13)]
        player_score = self.mancala[6] + sum(player_pits)
        opponent_score = self.mancala[13] + sum(opponent_pits)
        return player_score - opponent_score

#esta heuristica leva em consideração as peças que estão no lado do oponente e do jogador
# bem como a soma dessas peças com a pontuação já obtida

def get_heuristic3(self):
    if self.End():
        if self.mancala[13] > self.mancala[6]:
            return 100
        elif self.mancala[13] == self.mancala[6]:
            return 0
        else:
            return -100
    else:
        player_corner_pieces = self.mancala[5] + self.mancala[6]
        opponent_corner_pieces = self.mancala[12] + self.mancala[13]
        return player_corner_pieces - opponent_corner_pieces

#Esta função heurística calcula o número de peças  nos "Pits" mais proximos  do "pit" de pontuação do jogador e do adversário.
#A função retorna a diferença entre as peças no "pit" do jogador e do adversário.