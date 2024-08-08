class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9) ] # Nós usamos uma lista para representar o tabuleiro 3x3
        self.current_winner = None # mantenha o rastro do vencedor
        
        def print_board(self):
            for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
                print('| ' + ' | '.join(row) + ' |')
                
        @staticmethod
        def print_board_nums():
            # 0 | 1 | 2 etc (quando escolher um numero correspondente da caixa)
            number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
            for row in number_board:
                print('| ' + ' | '.join(row) + ' |')
        
        def available_move(self):
            # return []
            moves = []
            for (i, x) in enumerate(self)
            
                
            