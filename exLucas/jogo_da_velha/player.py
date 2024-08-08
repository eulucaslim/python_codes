import math
import random

class Player:
    def __init__(self, letter):
        # A letter é X ou O
        self.letter = letter
    
    # Nós queremos que todos os jogadores consigam dar um próximo passo
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        pass
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass