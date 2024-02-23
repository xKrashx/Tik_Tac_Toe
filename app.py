from tkinter import messagebox
from functools import partial
from tkinter import *
import game_state
import computer
import random
import ctypes

pc = None
count = 0
toggle = True
flip_flop = None
difficulty = None

def ClearWindow():
    for widget in window.winfo_children():
        widget.destroy()

def StartCallBack(vs_AI, dif=1):
    global pc, difficulty, flip_flop
    pc = vs_AI
    difficulty = dif
    if difficulty == 1:
        flip_flop = False
    if difficulty == 3:
        flip_flop = True
    ClearWindow()
    DrawBoard()

def Difficulty():
    ClearWindow()
    button = Button(window, text='Easy', height=3, width=5, bg='SystemButtonFace', font=('Halvetica', 20), command=lambda:StartCallBack(True, 1)).grid(row=0, column=0)
    button = Button(window, text='Medium', height=3, width=5, bg='SystemButtonFace', font=('Halvetica', 20), command=lambda:StartCallBack(True, 2)).grid(row=0, column=1)
    button = Button(window, text='Hard', height=3, width=5, bg='SystemButtonFace', font=('Halvetica', 20), command=lambda:StartCallBack(True, 3)).grid(row=0, column=2)

def DrawBoard():
    global buttons
    buttons = [[],[],[]]
    for i in range(3):
        for j in range(3):
            buttons[i].append(j)
            cmd = partial(MakeMove, i, j)
            
            # Wrong way to do it /Gives NoneType/
            # buttons[i][j] = Button(window, text=' ', height=3, width=5, bg='SystemButtonFace', font=('Halvetica', 20), command=cmd).grid(row=i, column=j)
            
            # Wright way to do it split them apart!!!
            buttons[i][j] = Button(window, text=' ', height=3, width=5, bg='SystemButtonFace', font=('Halvetica', 20), command=cmd)
            buttons[i][j].grid(row=i, column=j)

def MakeMove(i, j):
    global toggle, count, pc, flip_flop, difficulty
    
    if buttons[i][j]['text'] == ' ' and toggle:
        buttons[i][j]['text'] = 'X'
        buttons[i][j].config(state=DISABLED)
        game_state.update_board([i, j], 'hn')
        
    if buttons[i][j]['text'] == ' ' and not toggle:
        buttons[i][j]['text'] = 'O'
        buttons[i][j].config(state=DISABLED)
        game_state.update_board([i, j], 'ai')
        
    toggle = not toggle
    count += 1
    
    state = game_state.check_for_win()
    if state != None:
        if state == -1:
            ClearWindow()
            messagebox.showerror('End Game', 'X wins!')
            return
        if state == 1:
            ClearWindow()
            messagebox.showerror('End Game', 'O wins!')
            return
        if state == 0:
            ClearWindow()
            messagebox.showerror('End Game', 'Game ended in tie!')
            return

    if pc and not toggle:
        moves = game_state.get_possible_moves()
        move = None
        
        if flip_flop:
            move = computer.minimax_with_pruning(len(moves), True)[1]
        else:
            move = moves[random.randint(0, len(moves) - 1)]
            
        if difficulty == 2:
            flip_flop = not flip_flop
            
        MakeMove(move[0], move[1])

window = Tk()
window.title('Tic Tac Toe')

single = Button(window, text='AI', command=Difficulty)
double = Button(window, text='PvP', command=lambda:StartCallBack(False))
single.pack()
double.pack()

window.mainloop()