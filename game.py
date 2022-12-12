import copy
import pygame
from Variables import *
import time


def NegaMaxAlphaBetaPruning(game, player, depth, alpha, beta):
    
    if game.gameOver() or depth == 1:
        bestValue = game.evaluate()
        bestPit = None

        if player == -1 : #human
            bestValue = -bestValue
        return bestValue, bestPit
    bestValue = float('-inf')
    bestPit = None

    
    for pit in game.state.possibleMove(list(game.playerSide.keys())[list(game.playerSide.values()).index(player)]):
        child_game = copy.deepcopy(game)
        child_game.state.doMove(list(game.playerSide.keys())[list(game.playerSide.values()).index(player)], pit)
        print("Player ",list(game.playerSide.keys())[list(game.playerSide.values()).index(player)]," Played pit ",pit)
        value, _ = NegaMaxAlphaBetaPruning(child_game, -player, depth-1, -beta, -alpha)
        value = -value
        if value > bestValue:
            bestValue = value
            bestPit = pit
        if bestValue > alpha:
            alpha = bestValue
        if beta <= alpha:
            break
    return bestValue, bestPit


class  MancalaBoard:

    def __init__(self):
        # self.board = {  'A' : 0,'B' : 0,'C' : 0,'D' : 0,'E' : 0,'F' : 5,
        #                 'G' : 0,'H' : 1,'I' : 0,'J' : 0,'K' : 1,'L' : 0,
        #                 'M1' : 0, 'M2' : 0
        #              }
        self.board = {  'A' : 4,'B' : 4,'C' : 4,'D' : 4,'E' : 4,'F' : 4,
                        'G' : 4,'H' : 4,'I' : 4,'J' : 4,'K' : 4,'L' : 4,
                        'M1' : 0, 'M2' : 0
                     }
        self.index_player_1 = ['A', 'B', 'C', 'D', 'E', 'F']
        self.index_player_2 = ['G', 'H' , 'I', 'J', 'K', 'L']

        self.fosse_opp = {  
                            'A' : 'G', 'B' : 'H', 'C' : 'I','D' : 'J', 'E' : 'K', 'F' : 'L',
                            'G' : 'A', 'H' : 'B', 'I' : 'C','J' : 'D', 'K' : 'E', 'L' : 'F',
                        }
        self.fosse_suiv_player_1 = {  
                            'A' : 'B', 'B' : 'C', 'C' : 'D','D' : 'E', 'E' : 'F', 'F' : 'M1', 'M1' : 'G',
                            'G' : 'H', 'H' : 'I', 'I' : 'J','J' : 'K', 'K' : 'L', 'L' : 'A',
                        }
        self.fosse_suiv_player_2 = {  
                            'A' : 'B', 'B' : 'C', 'C' : 'D','D' : 'E', 'E' : 'F', 'F' : 'G',
                            'G' : 'H', 'H' : 'I', 'I' : 'J','J' : 'K', 'K' : 'L', 'L' : 'M2', 'M2' : 'A'
                        }
    
    def possibleMove(self, player):
        possible_moves = []
        if player == 1 :
            for  pos in self.index_player_1:
                if self.board[pos] > 0 : 
                    possible_moves.append(pos)
            return possible_moves
        else :
            for  pos in self.index_player_2:
                if self.board[pos] > 0 : 
                    possible_moves.append(pos)
            return possible_moves
        
    def doMove(self, player, Pit):

        if player == 1 :
            seed = self.board[Pit]
            self.board[Pit] = 0
            for i in range(seed):
                self.board[self.fosse_suiv_player_1[Pit]] += 1
                Pit = self.fosse_suiv_player_1[Pit]
        elif player == 2:
            seed = self.board[Pit]
            self.board[Pit] = 0
            for i in range(seed):
                self.board[self.fosse_suiv_player_2[Pit]] += 1
                Pit = self.fosse_suiv_player_2[Pit]

        if (player == 1 and Pit == 'M1') or (player == 2 and Pit == 'M2') :
            return player
        elif player == 1 :
            return 2
        elif player == 2 :
            return 1

    def draw(self):
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 25)
        
        x = 500
        offset = 180
        
        # Affichage des magsins

        rect = pygame.Rect((Width/8,Hight/3), (150, 300))
        pygame.draw.rect(window, PitColor, rect, 1, 5)
        rect = pygame.Rect((4* Width/5,Hight/3), (150, 300))
        pygame.draw.rect(window, PitColor, rect, 1, 5)
        
        text = font.render("M2", True, PitColor)
        window.blit(text, (300,650))
        text = font.render(str(self.board["M2"]), True, PitColor)
        window.blit(text, (300,500))
        
        text = font.render("M1", True, PitColor)
        window.blit(text, (1600, 650))
        text = font.render(str(self.board["M1"]), True, PitColor)
        window.blit(text, (1600,500))

        pygame.draw.circle(window, PitColor, (x, 420), 50, 2)
        pygame.draw.circle(window, PitColor, (x, 570), 50, 2)
        text = font.render("G", True, PitColor)
        window.blit(text, (x, 300))
        text = font.render(str(self.board["G"]), True, PitColor)
        window.blit(text, (x, 400))
        
        text = font.render("A", True, PitColor)
        window.blit(text, (x, 650))
        text = font.render(str(self.board["A"]), True, PitColor)
        window.blit(text, (x, 550))


        x += offset
        pygame.draw.circle(window, PitColor, (x, 420), 50, 2)
        pygame.draw.circle(window, PitColor, (x, 570), 50, 2)
        text = font.render("H", True, PitColor)
        window.blit(text, (x, 300))
        text = font.render(str(self.board["H"]), True, PitColor)
        window.blit(text, (x, 400))
        text = font.render("B", True, PitColor)
        window.blit(text, (x, 650))
        text = font.render(str(self.board["B"]), True, PitColor)
        window.blit(text, (x, 550))


        x += offset
        pygame.draw.circle(window, PitColor, (x, 420), 50, 2)
        pygame.draw.circle(window, PitColor, (x, 570), 50, 2)
        text = font.render("I", True, PitColor)
        window.blit(text, (x, 300))
        text = font.render(str(self.board["I"]), True, PitColor)
        window.blit(text, (x, 400))
        text = font.render("C", True, PitColor)
        window.blit(text, (x, 650))
        text = font.render(str(self.board["C"]), True, PitColor)
        window.blit(text, (x, 550))

        x += offset
        pygame.draw.circle(window, PitColor, (x, 420), 50, 2)
        pygame.draw.circle(window, PitColor, (x, 570), 50, 2)
        text = font.render("J", True, PitColor)
        window.blit(text, (x, 300))
        text = font.render(str(self.board["J"]), True, PitColor)
        window.blit(text, (x, 400))
        text = font.render("D", True, PitColor)
        window.blit(text, (x, 650))
        text = font.render(str(self.board["D"]), True, PitColor)
        window.blit(text, (x, 550))
        
        x += offset
        pygame.draw.circle(window, PitColor, (x, 420), 50, 2)
        pygame.draw.circle(window, PitColor, (x, 570), 50, 2)
        text = font.render("K", True, PitColor)
        window.blit(text, (x, 300))
        text = font.render(str(self.board["K"]), True, PitColor)
        window.blit(text, (x, 400))
        text = font.render("E", True, PitColor)
        window.blit(text, (x, 650))
        text = font.render(str(self.board["E"]), True, PitColor)
        window.blit(text, (x, 550))

        x += offset
        pygame.draw.circle(window, PitColor, (x, 420), 50, 2)
        pygame.draw.circle(window, PitColor, (x, 570), 50, 2)
        text = font.render("L", True, PitColor)
        window.blit(text, (x, 300))
        text = font.render(str(self.board["L"]), True, PitColor)
        window.blit(text, (x, 400))
        text = font.render("F", True, PitColor)
        window.blit(text, (x, 650))
        text = font.render(str(self.board["F"]), True, PitColor)
        window.blit(text, (x, 550))

class Game: 

    def __init__(self, board : MancalaBoard, player):
        self.state = board
        self.playerSide = {1 : 1, 2 : -1}
        self.alpha = float('-inf')
        self.beta = float('inf')

    def gameOver(self):
        
        all_zero_1 = True
        for index in self.state.index_player_1:
            if self.state.board[index] != 0: 
                all_zero_1 = False
                break
        
        all_zero_2 = True
        for index in self.state.index_player_2:
            if self.state.board[index] != 0: 
                all_zero_2 = False
                break

        if not all_zero_1 and not all_zero_2 : return False
        
        # get all the left seeds for player 2
        count = 0
        if all_zero_1 :
            for index in self.state.index_player_2:
                count += self.state.board[index]
                self.state.board[index] = 0
            self.state.board['M2'] += count

        # get all the left seeds for player 1
        count = 0
        if all_zero_2 :
            for index in self.state.index_player_1:
                count += self.state.board[index]
                self.state.board[index] = 0
            self.state.board['M1'] += count

        return True

    def findWinner(self):

        if self.state.board['M1'] > self.state.board['M2'] :
            return 1, self.state.board['M1']      #player 1 won
        elif self.state.board['M1'] < self.state.board['M2'] : 
            return 2, self.state.board['M2']   #player 2 won

    def evaluate(self):
        return (self.state.board["M1"] - self.state.board["M2"])
            
        
class Play:

    def humanTurn(state :Game, curent_player):
        
        print(state.state.possibleMove(curent_player))
        move = input("Selectionez parmis les choix :")
        
        curent_player = state.state.doMove(curent_player, move)
        return curent_player

    def computerTurn(game : Game, curent_player, depth = 6 ):
        if len(game.state.possibleMove(curent_player)) > 0:
            best_node = NegaMaxAlphaBetaPruning(game, game.playerSide[curent_player], depth, game.alpha, game.beta)
            curent_player = game.state.doMove(curent_player, best_node[1])

        return curent_player, game


    