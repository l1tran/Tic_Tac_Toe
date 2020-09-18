import game_func as g
#----------------------------------------Class Vars-----------------------------------------------
class Vars:
    used_nums =" "
    winner = None
    player = '-'
    game_continue = True
    comp = None
    board = ['-','-','-','-','-','-','-','-','-']
    first =  None
#------------------------------------------Get Input-------------------------------------------------
g.os.system('clear')
'''
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
    b.print_board(vars.board)
    
#-----------------------------------Check win condition-------------------------------------
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

#---------------------------------------Cpu Turn----------------------------------------
os.system('clear')
def cpu_turn(vars):
    result2 = " "
    while True:
        result2 = str(random.randint(0,8))
        if result2 not in vars.used_nums:
            vars.used_nums =  vars.used_nums + result2
            vars.board[int(result2)] = vars.comp
            time.sleep(0.5)
            b.print_board(vars.board)
            break
'''
#----------------------------------------Main--------------------------------------------
def loop_game(vars):
    while True:
        game(vars)

def game(vars):
    g.os.system('clear')
    print("==@====@====@====@====@==")
    print(" |@|   TIC TAC TOE   |@|")
    print("==@====@====@====@====@==\n")
    input("Press any key to start")
    g.print_board(vars.board)
    while vars.player.upper() != 'X' and vars.player.upper() != 'O':
        vars.player = input("Enter 'X' or 'O': ").upper()
        print("You chose: ", vars.player)
        g.time.sleep(1)    
    if vars.player == 'X':
        vars.comp = 'O'
    else:
        vars.comp = 'X'

    g.print_board(vars.board)

    while vars.first != 'yes' and vars.first != 'no':
        vars.first = input("Would you like to go first?\nIf so type 'yes' otherwise type 'no': ")

    while vars.game_continue:
        if vars.first == 'yes':
            g.get_input(vars)
        else:
            g.cpu_turn(vars)
        g.check_win(vars)
        if vars.game_continue == False:
            break
        #------------Flip to other player----------
        if vars.first == 'yes':
            g.cpu_turn(vars)
        else:
            g.get_input(vars)
        g.check_win(vars)
    if vars.winner == 'X' or vars.winner == 'O':
        if vars.winner == vars.player:
            print("YOU WON!!")
        else:
            print("Uh oh you Lost, better luck next time!!")
    elif vars.winner == None:
        print("Tie")
    while True:
        restart = input("Do you want to try again? Type 'yes' or 'no': ")
        if restart == 'no':
            print("Bye bye~")
            g.time.sleep(1)
            quit()
        elif restart == 'yes':
            g.os.system('clear')
            vars.used_nums =" "
            vars.winner = None
            vars.player = '-'
            vars.game_continue = True
            vars.comp = None
            vars.board = ['-','-','-','-','-','-','-','-','-']
            vars.first =  None
            break

if __name__ == '__main__':
    loop_game(Vars)