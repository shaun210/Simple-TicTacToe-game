import random


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def action(number,theBoard):
    if number == 'X':
        alternate = '0'
    elif number == '0':
        alternate = 'X'
    
    for i in range(9):
        
        flag1 = False 
        flag2 = False
        while flag1 == False:
            print("enter a number from 1 to 9. Board is like a telephone dial")
            numI = input()          
            if theBoard[numI] == ' ' and theBoard[numI] != alternate :
                theBoard[numI] = number
                flag1 = True
                
                if checkWin(theBoard, number):
                    return theBoard  
                flag2 = False
                while flag2 == False:
                    n = random.randint(1,9)
                    if theBoard[str(n)] == ' ' and theBoard[str(n)] != number:
                        theBoard[str(n)] = alternate
                        flag2 = True
                        
            else:
                print("invalid number")  

            if checkWin(theBoard, number):
                return theBoard  
            printBoard(theBoard)
    return theBoard 


def game(board):
    print("do you want to be either X or 0")
    answer = input()
    if answer == "x":
        answer.capitalize
    if(answer == "X" or answer == "0"):
        action(answer, board)
    else:
        print("wrong input")  

def checkWin(theBoard, turn):
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
        printBoard(theBoard)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")                
        return True
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
        printBoard(theBoard)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        return True       
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
        printBoard(theBoard)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        return True        
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
        printBoard(theBoard)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        return True
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
        printBoard(theBoard)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        return True
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
        printBoard(theBoard)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        return True
    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
        printBoard(theBoard)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        return True
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
        printBoard(theBoard)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        return True
    else:
        return False

def main():

    theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                '4': ' ' , '5': ' ' , '6': ' ' ,
                '1': ' ' , '2': ' ' , '3': ' ' }

    game(theBoard)

if __name__ == "__main__":
    main()