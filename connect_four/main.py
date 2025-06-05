
from collections import deque
from enum import Enum
import random
class GameState(Enum):
    PLAYING="PLAYING"
    WON="WON"
    DRAW="DRAW"
class Game:
    def __init__(self,name,players,board):
        self.name=name
        self.board=board
        self.players=players
        self.valid=True
        self.game_state=GameState.PLAYING
    def start_game(self):
        
        player_index=0
        player=self.players[random.randint(0,len(self.players)-1)]
        move=self.get_valid_move(player,self.board)
        while self.game_state==GameState.PLAYING:

            self.board.make_move(player,move)
            self.game_won_check(self.board,player)
            self.game_draw_check(self.board)
            if self.game_state==GameState.DRAW:
                print(f"\n--Game Over--\n The game ended in a draw. Thank you for your participation:\n")
                print({player.name for player in self.players})
                break
            if self.game_state==GameState.WON:
                print(f"\n--Game Over--\n The game ended in a Win. Congratulations {player.name} Thank you for your participation:\n")
                print({player.name for player in self.players})
                for participant in self.players:
                    if participant==player:
                        player.games_won+=1
                    else:
                        participant.games_lost+=1
                    player.get_stats()
                break
            if player_index==len(self.players)-1:
                player_index=0
            else:
                player_index+=1
            player=self.players[player_index]
            move=self.get_valid_move(player,self.board)
            

    def game_won_check(self, board, player):
            ROWS, COLS = len(board.board), len(board.board[0])
            symbol = player.symbol

            for r in range(ROWS):
                for c in range(COLS):
                    if board.board[r][c] == symbol: 
                        
                        # For each direction, we check 3 more cells to make a total of 4
                        directions = [[0, 1],  # Horizontal right
                                    [0, -1], # Horizontal left
                                    [1, 0],  # Vertical down
                                    [-1, 0]] # Vertical up
                                    # diagonals are like below:
                                    # [1, 1], [1, -1], [-1, 1], [-1, -1] 

                        for dr, dc in directions: 
                            count = 1 # Start with 1 for the current cell (r, c)

                            # Check the next 3 cells in this direction
                            for step in range(1, 4):
                                next_r, next_c = r + dr * step, c + dc * step

                                if self.connection_check(symbol, board, next_r, next_c) == 1:
                                    count += 1
                                else:
                                    # stop checking this direction
                                    break 
                            
                            if count == 4:
                                self.game_state = GameState.WON
                                return self.game_state 

            return self.game_state 
    def connection_check(self,symbol,board,row,col):
        ROWS,COLS=len(board.board),len(board.board[0])
        if min(row,col)<0 or row>=ROWS or col>=COLS:
            return 0
        if board.board[row][col]==symbol:
            return 1
        return 0
       

    def game_draw_check(self,board):
        r,c=0,0
        while r<len(board.board):
            c=0
            while c<len(board.board[0]):
                if board.board[r][c]=="_":                
                    return self.game_state
                c+=1
            r+=1
        self.game_state=GameState.DRAW
        return self.game_state
    def get_valid_move(self,player,board): 
        while True:  # Keep looping indefinitely
            try:
                inputed = input(f"{player.name}, please type your move (column number 0-6): ")
                move = int(inputed) # Attempt to convert to an integer
                if not (0 <= move <= 6):
                    print("Invalid column number. Please enter a number between 0 and 6.")
                    continue # Go back to the start of the loop
                if board.board[0][move]!="_":
                    print("The column you entered is full, Try another one.")
                    continue
                return move # If conversion and validation are successful, exit the loop and return the move

            except ValueError:
                # This block runs if int(inputed) fails (e.g., user types text)
                print("That's not a valid number. Please enter a numerical column (e.g., 3).")
                # The loop will then repeat, asking for input again

            except Exception as e:
                # Catch any other unexpected errors, though ValueError is most common here
                print(f"An unexpected error occurred: {e}")
                print("Please try again.")
                # The loop will still repeat

           
    

class Player:
    def __init__(self,name,symbol):
        self.name=name
        self.symbol=symbol
        self.games_won=0
        self.games_lost=0
    def get_stats(self):
        print("player_stats")
        print(f"player: {self.name} has won {self.games_won} and lost {self.games_lost}")
    
class Board:
    def __init__(self):
        self.board=list(["_"]*7 for i in range(6))

    def make_move(self,player,move):
        available_row=self.get_valid_position(move)
            
        self.board[available_row][move]= player.symbol
        print("\n")
        print(self.board)
        print("\n")
        # return self.board
        
    def get_valid_position(self,column):
        temp_row=len(self.board)-1
        position=self.board[temp_row][column]
        
        while position!="_":
            temp_row-=1
            position=self.board[temp_row][column]
        return temp_row
        
first_board=Board()

jer=Player("Jeremy","J")
rira=Player("Wachira","W")
our_game=Game("first_game",[jer,rira],first_board)
our_game.start_game()