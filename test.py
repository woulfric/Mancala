
board = {  'A' : 1,'B' : 0,'C' : 5,'D' : 4,'E' : 8,'F' : 0,
            'G' : 4,'H' : 4,'I' : 4,'J' : 4,'K' : 4,'L' : 4,
            'M1' : 0, 'M2' : 0
        }

index_player_1 = ['A', 'B', 'C', 'D', 'E', 'F']
index_player_2 = ('G', 'H' , 'I', 'J', 'K', 'L')


def possibleMove(player):
        possible_moves = []
        if player == 1 :
            for  pos in index_player_1:
                if board[pos] > 0 : 
                    possible_moves.append(pos)
            return possible_moves
        else :
            for  pos in index_player_2:
                if board[pos] > 0 : 
                    possible_moves.append(pos)
            return possible_moves
        

print(possibleMove(1))