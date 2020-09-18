import os
import random
import time
#---------------------------------------Print Board---------------------------------------------
def print_board(board):
    os.system('clear')
    print("=====================")
    print("#  " + board[0] + "|" + board[1] + "|" + board[2] + '     1|2|3  #')
    print("#  " + board[3] + "|" + board[4] + "|" + board[5] + '     4|5|6  #')
    print("#  " + board[6] + "|" + board[7] + "|" + board[8] + '     7|8|9  #')
    print("=====================")
#------------------------------------------Get Input--------------------------------------------   
def get_input(vars):
    result = "0"
    while not result.isdigit() or len(result) != 1 or int(result)>=10 or int(result)<=0 or str((int(result)-1)) in vars.used_nums:
        os.system('cls')
        print_board(vars.board)
        if result.isdigit():
            if str(int(result)-1) in vars.used_nums:
                result = input("Spot already filled: ")
            else:
                result = input("Enter a number from 1-9: ")
        else:
            result = input('Please enter a number between 1-9: ')    
    result = int(result) - 1
    vars.used_nums =  vars.used_nums + str(result) 
    vars.board[result] = vars.player
    print_board(vars.board)
    
#-----------------------------------Check win condition-----------------------------------------
os.system('clear')
def check_tie(vars):
    if '-' not in vars.board:
        vars.game_continue = False

def check_rows(vars):
    row_1 = vars.board[0] == vars.board[1] == vars.board[2] != "-"
    row_2 = vars.board[3] == vars.board[4] == vars.board[5] != "-"
    row_3 = vars.board[6] == vars.board[7] == vars.board[8] != "-"
    if row_1 or row_2 or row_3:
        vars.game_continue = False
    if row_1:
        return vars.board[0]
    elif row_2:
        return vars.board[3]
    elif row_3:
        return vars.board[6]

def check_cols(vars):
    col_1 = vars.board[0] == vars.board[3] == vars.board[6] != "-"
    col_2 = vars.board[1] == vars.board[4] == vars.board[7] != "-"
    col_3 = vars.board[2] == vars.board[5] == vars.board[8] != "-"
    if col_1 or col_2 or col_3:
        vars.game_continue = False
    if col_1:
        return vars.board[0]
    elif col_2:
        return vars.board[1]
    elif col_3:
        return vars.board[2]

def check_diags(vars):
    diag_1 = vars.board[0] == vars.board[4] == vars.board[8] != "-"
    diag_2 = vars.board[2] == vars.board[4] == vars.board[6] != "-"
    if diag_1 or diag_2:
        vars.game_continue = False
    if diag_1:
        return vars.board[0]
    elif diag_2:
        return vars.board[2]

def check_win(vars):
    vars.winner = check_rows(vars) or check_cols(vars) or check_diags(vars) or check_tie(vars) != None

#---------------------------------------Cpu Turn------------------------------------------
os.system('clear')
def cpu_turn(vars):
    result2 = " "
    while True:
        result2 = str(random.randint(0,8))
        if result2 not in vars.used_nums:
            vars.used_nums =  vars.used_nums + result2
            vars.board[int(result2)] = vars.comp
            time.sleep(0.5)
            print_board(vars.board)
            break