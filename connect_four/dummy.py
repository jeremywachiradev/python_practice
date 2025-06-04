
def play_game(moves):
    board=list(["_"]*7 for i in range(6))
    turn_change=True
    print(board[1][2])

    for move in moves:
        available_row=len(board)-1
        while board[available_row][move]!="_":
            available_row-=1
        board[available_row][move]="Y" if turn_change else "R"
        turn_change= not turn_change


    print(board)
# whatever is passed in this function is actually just the moves the players are making i.e. the first value is the first move the first player "Y" makes then the second is the 2nd player's "R" first move  
play_game([0,1,2,5,6,2,0,0])