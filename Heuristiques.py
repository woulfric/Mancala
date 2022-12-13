import copy

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