class Board:
    def __init__(self): # constructor
        self.rows, self.cols = 6,7
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def display_board(self): # a method to display the board status
        print(" ".join(str(num) for num in range(self.cols)))
        for row in self.board:
            after_join=" ".join(str(elem) for elem in row)
            print(after_join)

    def get_valid_moves(self): # a method that return a list of valid moves
        valid_moves=[]
        for col in range(self.cols):
            if self.board[0][col]==0 :
                valid_moves.append(col) 

        return valid_moves

    def make_move(self,col,player): # a method to make a move, col is the colomn that the player choosed, player can be 1 (red) or 2 (yellow)
        if col not in self.get_valid_moves():
            return False
        else:
            for row in range(self.rows-1,-1,-1):
                if self.board[row][col]==0:
                    self.board[row][col]=player
                    return True

    def check_winner(self,player):
        for col in range(self.cols):    #Check four consecutive pieces vertically
            for row in range(self.rows-3):      
                if self.board[row][col]==player and self.board[row+1][col]==player and self.board[row+2][col]==player and self.board[row+3][col]==player:
                    return True

        for row in range(self.rows):    #Check four consecutive pieces horizontally
            for col in range(self.cols-3):       
                if self.board[row][col]==player and self.board[row][col+1]==player and self.board[row][col+2]==player and self.board[row][col+3]==player:
                    return True

        for row in range(self.rows-3):  #Check four consecutive pieces diagonally top-left to bottom-right
            for col in range(self.cols-3):
                  if self.board[row][col]==player and self.board[row+1][col+1]==player and self.board[row+2][col+2]==player and self.board[row+3][col+3]==player:
                      return True

        for row in range(self.rows-3):   #Check four consecutive pieces diagonally top-right to bottom-left
            for col in range(3,self.cols):
                if self.board[row][col]==player and self.board[row+1][col-1]==player and self.board[row+2][col-2]==player and self.board[row+3][col-3]==player:
                    return True

        return False

    def is_draw(self):
        if self.get_valid_moves()==[]: #check if there is no more moves to do -> draw
            return True
        
        return False



#=======================================
# i did not implement the AI vs human yet

        

