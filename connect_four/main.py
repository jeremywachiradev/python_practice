
from collections import deque
import random
class Game:
    def __init__(self,name,players,board):
        self.name=name
        self.board=Board()
        self.players=players
        self.valid=True
    def start_game(self):
        # number_of_players=len(self.players)
        # first_player_index=random.choice(0,number_of_players)
        # player=self.players[first_player_index]
        # handle random selection of the first index
        player_index=0
        player=self.players[player_index]
        inputed=input(f"{player.name} please type a move: ")
        move=int(inputed)

        self.board.make_move(player,player_index,self.players,move)

class Player:
    def __init__(self,name,symbol):
        self.name=""
        self.symbol=""
        self.games_won=0
        self.games_lost=0
    def get_stats(self,player_name):
        print(self.name,self.games_won,self.games_lost)
    
class Board:
    def __init__(self):
        self.board=list(["_"]*7 for i in range(6))

    def make_move(self,player,player_index,players,move):
        available_row=len(self.board)-1
        while self.board[available_row][move]!="_":
            available_row-=1
        if available_row<0:
            return "Full column"
        self.board[available_row][move]= player.symbol
        print("\n")
        print(self.board)
        print("\n")
        if self.is_won(self.board,player.symbol):
            return f"---Game Over--- \n Congratualtions {player.name} Thank you for your participation:"

        elif self.is_draw(self.board):
            self.is_draw(self.board)
            return f"---Game Over--- \n It's a draw, Thank you for your participation: "
            
        
        else:
            if player_index<len(players)-1:
                player_index+=1
            else:
                player_index=0
            player=players[player_index]
            move=int(input(f"{player.name} please type a move:"))
            
            self.make_move(player,player_index,players,move)
        
    def is_draw(self,board):
        r,c=0,0
        while r<len(board):
            while c<len(board[0]):
                
                if board[r][c]=="_":
                    return False
        return True
    def is_won(self,board,symbol):
        ROWS,COLS=len(board),len(board[0])
        row,col=0,0
        connected=0
        my_queue=deque()
        visited=set()
        my_queue.append((row,col))
        # visited.add((row,col))
        while my_queue:
            for i in range(len(my_queue)):
            
                if connected==4:
                    return True
                my_queue.popleft()
                directions=[[0,1],[0,-1],[1,0],[-1,0]]
                for r,c in directions:
                    if min(row+r,col+c)<0 or board[row+r][col+c]!= symbol or (row+r,col+c) in visited or row+r==ROWS or col+c==COLS:
                        continue
                    my_queue.append((r,c))
            connected+=1
        return False
first_board=Board()

jer=Player("Jeremy","J")
rira=Player("Wachira","W")
our_game=Game("first_game",[jer,rira],first_board)
our_game.start_game()