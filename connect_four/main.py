"""
game: takes in a move  and update board 
board
"""
def play_game(moves):
    board=list(["_"]*7 for i in range(6))
    turn_change=True
    print(board[1][2])

    for move in moves:
        available_row=len(board)-1
        # print(board[available_row][move])
        while board[available_row][move]!="_":
            available_row-=1
        board[available_row][move]="Y" if turn_change else "R"
        turn_change= not turn_change


    print(board)

play_game([0,1,2,5,6,2,0,0])