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
g.os.system('clear')
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