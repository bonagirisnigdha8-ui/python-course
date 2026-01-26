#Implementation of Two Player Tic-Tac-Toe game in Python.
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
board_keys = []

for key in theBoard:
    board_keys.append(key)

    def printboard(board)
        print(board['7']+'|'+ board['8']+|+ board['9'])
        print('-+-+-')
        print(board['4']+'|'+ board['5']+|+ board['6'])
        print('-+-+-')
        print(board['4']+'|'+ board['5']+|+ board['6'])
        print('-+-+-')
        print(board['1']+'|'+ board['2']+|+ board['3'])
        print('-+-+-')

        #Now we will write the main function which has all the gameplay functionally.
        def game():

            turn = 'X'
            count = 0

            for i in range(10):
                printBoard(theBoard)
                print("It's your turn"+turn+"where do you want to move?")

                move = input()
            
                if theBoard [move] == '':
                    theBoard[move] = turn
                    count += 1
                else:
                    print("That place is already filled.\nMove to which place?")
                    continue
                #Now we will check if player X or O has won after 5 moves.
                if count >=5:
                     
