import game_state
import math

def minimax(depth, isMaximizing):
    bestMove = 0
    result = game_state.check_for_win()

    if depth == 0 or result != None:
        return [game_state.evaluate(), -1]

    if isMaximizing:
        maxEval = -math.inf
        for move in game_state.get_possible_moves():
            game_state.update_board(move, 'ai')
            evaluation = minimax(depth - 1, False)
            game_state.undo(move)
            if evaluation[0] > maxEval:
                maxEval = evaluation[0]
                bestMove = move
        return [maxEval, bestMove]

    else:
        minEval = math.inf
        for move in game_state.get_possible_moves():
            game_state.update_board(move, 'hn')
            evaluation = minimax(depth - 1, True)
            game_state.undo(move)
            if evaluation[0] < minEval:
                minEval = evaluation[0]
                bestMove = move
        return [minEval, bestMove]

def minimax_with_pruning(depth, isMaximizing, alpha=-math.inf, beta=math.inf):
    bestMove = 0
    result = game_state.check_for_win()
    
    if depth == 0 or result != None:
        return [game_state.evaluate(), -1]

    if isMaximizing:
        maxEval = -math.inf
        for move in game_state.get_possible_moves():
            game_state.update_board(move, 'ai')
            evaluation = minimax(depth - 1, False)
            game_state.undo(move)
            if evaluation[0] > maxEval:
                maxEval = evaluation[0]
                bestMove = move
            alpha = max(alpha, evaluation[0])
            if beta <= alpha:
                break
        return [maxEval, bestMove]

    else:
        minEval = math.inf
        for move in game_state.get_possible_moves():
            game_state.update_board(move, 'hn')
            evaluation = minimax(depth - 1, True)
            game_state.undo(move)
            if evaluation[0] < minEval:
                minEval = evaluation[0]
                bestMove = move
            beta = min(beta, evaluation[0])
            if beta <= alpha:
                break
        return [minEval, bestMove]