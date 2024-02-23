board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

players = {
    'hn': 'X',
    'ai': 'O'
}

def check_for_win():
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0] == players['hn']: return -1
        else: return 1
    if board[1][0] == board[1][1] and board[1][1] == board[1][2]: 
        if board[1][0] == players['hn']: return -1
        else: return 1
    if board[2][0] == board[2][1] and board[2][1] == board[2][2]: 
        if board[2][0] == players['hn']: return -1
        else: return 1
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]: 
        if board[0][0] == players['hn']: return -1
        else: return 1
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]: 
        if board[0][1] == players['hn']: return -1
        else: return 1
    if board[0][2] == board[1][2] and board[1][2] == board[2][2]: 
        if board[0][2] == players['hn']: return -1
        else: return 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]: 
        if board[0][0] == players['hn']: return -1
        else: return 1
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]: 
        if board[0][2] == players['hn']: return -1
        else: return 1
        
    flag = True
    for row in board:
        for column in row:
            if column != players['hn'] and column != players['ai']:
                flag = False
                break
        else:
            continue
        break
    
    if flag: return 0
    return None

def get_possible_moves():
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != players['hn'] and board[i][j] != players['ai']: free.append([i, j])
    return free

def update_board(position, player):
    board[position[0]][position[1]] = players[player]

def undo(position):
    board[position[0]][position[1]] = position[1] + 3 * position[0] + 1

def show_game_state():
    import os
    os.system('cls')
    print("{}|{}|{}\n-|-|-\n{}|{}|{}\n-|-|-\n{}|{}|{}".format(board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]))

def evaluate():
    score = 0
    score += evaluate_line([0, 0], [0, 1], [0, 2])
    score += evaluate_line([1, 0], [1, 1], [1, 2])
    score += evaluate_line([2, 0], [2, 1], [2, 2])
    score += evaluate_line([0, 0], [1, 0], [2, 0])
    score += evaluate_line([0, 1], [1, 1], [2, 1])
    score += evaluate_line([0, 2], [1, 2], [2, 2])
    score += evaluate_line([0, 0], [1, 1], [2, 2])
    score += evaluate_line([0, 2], [1, 1], [2, 0])
    return score

def evaluate_line(cell_1, cell_2, cell_3):
    score = 0
 
    if board[cell_1[0]][cell_1[1]] == players['ai']: score = 1
    elif board[cell_1[0]][cell_1[1]] == players['hn']: score = -1
 
    if board[cell_2[0]][cell_2[1]] == players['ai']:
        if score == 1: score = 10
        elif score == -1: return 0
        else: score = 1
    elif board[cell_2[0]][cell_2[1]] == players['hn']:
        if score == -1: score = -10;
        elif score == 1: return 0
        else: score = -1

    if board[cell_3[0]][cell_3[1]] == players['ai']:
        if score > 0: score *= 10
        elif score < 0: return 0
        else: score = 1
    elif board[cell_3[0]][cell_3[1]] == players['hn']:
        if score < 0: score *= 10
        elif score > 1: return 0
        else: score = -1

    return score