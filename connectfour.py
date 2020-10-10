"""
Author:  Ify Jacob
Date:    4/27/2020
Description: The file allows th user to play a game of connect four with another person or computer
"""

from random import randint

class AdjoinTheSpheres:
    
    def __init__(self):
        #Descided to make the players the objects in the class
        self.player_1 = "x"
        self.player_2 = "o"

    def main_menu(self):
        #The Main Menu of the game that returns only 1,2, or 3
        print("AdjoinTheSpheres Main Menu")
        print("\t1) New Game (2 player)")
        print("\t2) New Game (1 player vs computer)")
        print("\t3) Exit Game")

        options = [1,2,3]
        option = int(input("Select Option from the Menu: " ))
        while option not in options:
            print("Invalid choice, try again.")
            option = int(input("Select Option from the Menu: " ))                                                                        
        return option
    
    def create_board(self,the_file):
        #The function reads in the boards line by line and puts them in a list
        board_list = []
        board = []
        my_file = input("What game/map do you want to load? ")
        the_file = open(my_file,"r") 
        the_file = the_file.readlines()
        
        for line in the_file:
            line = line.strip("\n")
            if line !="":
                board_list.append(line)
        return board_list
    
    def load_board(self,board_list):
        #The real board is the part of the board that includes the actually index and piece on the board and excludes the first two lines
        real_board = board_list[2:]
        first_board = board_list[0]

        #Creates the bounds given the row and col given in the first line of the file that was read in
        board_list[0] = board_list[0].split(" ")
        num_row = int(board_list[0][0])
        num_col = int(board_list[0][1])

        #Formaula for the dashed line incase the board isn't always 5 by 7
        display_line = ""
        for i in range((num_col*2)+1):
            if i < 2:
                display_line += " "
            else:
                display_line += "-"

        #The rest of the code creates the board that the user see's with the dashed lines, rows, and col and returns "move_board" which is the initally read in file
        col_string = ""
        for j in range(num_col):
            top_display = str((j+1))
            col_string += top_display
            
        col_string = "|".join(col_string)
        col_string = "  " + col_string
        print(col_string)
        print(display_line)
        
        for i in range(len(real_board)):
            board = "|".join(real_board[i])
            row_display = str(i+1) + " "
            board = row_display + board
            
            print(board)
            print(display_line)

        move_board = []
        move_board.append(first_board)
        move_board.append(board_list[1])
        for i in range(len(real_board)):
            move_board.append(list(real_board[i]))

        return move_board
    
    def save_board(self,saved_board,current_player):
        #The function saves the current board if called and overwrites the any file with the same named used during the save
        board_list = []
        the_file = input("What would you like to save the game as? ")
        save_file = open(the_file,"w")

        string = ""
        for i in range(len(saved_board)):
            for j in range(len(saved_board[i])):
                saved_board[1] = current_player              
                string = string + saved_board[i][j]
                
            save_file.write(string)
            save_file.write("\n")

            string = ""    
        save_file.close
        return the_file

    def show_saved_board(self,the_file):
        #This function show the board that was just saved (similarly to the creat board function without asking the questions)
        board_list = []
        load_file = open(the_file,"r") 
        load_file = load_file.readlines()
        
        for line in load_file:
            line = line.strip("\n")
            if line !="":
                board_list.append(line)
        return board_list
    
    def turn_flow(self,current_player):
        #Determines the turn flow of each player once a move has been made and changes the current player if conditions in valid move have been meet
        if current_player == self.player_1:
            current_player = self.player_2
            return current_player
        
        else:
            current_player = self.player_1
            return current_player
        
    def valid_move(self,current_board,move,player):
        #The function determines if the move made by a player is valid by checking if it's in range and that there's not already a piece in its place
        current_player = player
        valid_move = False
        
        for i in range(len(current_board)):
            row_bound = len(current_board) -1
            
            for j in range(len(current_board[i])):
                col_bound = len(current_board[i]) - 1
                                                                                                        
        if len(move) == 3 and move[1] == " ":
            area = move.split(" ")
            row = int(area[0]) + 1
            col = int(area[1]) - 1
            
            if row <= row_bound and col <= col_bound:
                
                if current_board[row][col] ==" ":
                    current_board[row][col] = current_player
                    valid_move = True
                elif current_board[row][col] =="*":
                    valid_move = False
                else:
                    valid_move = False

            else:
                valid_move = False
        #Returns a list consisting of the new board and a Boolean which if True will allow the game to continue
        #if False makes the current player redo their turn
        validation = []
        validation.append(current_board)
        validation.append(valid_move)                                            
        return validation

    def connect_four(self,board):
        #The Function reads in the current board and checks to all possible cases of connect four being meant and returns a boolean depending on the result
        connect_four = False
        board = board[2:]

        #set boundaries to determine if a certain index is in range
        for i in range(len(board)):            
            row_bound = len(board) -1
                            
            for j in range(len(board[i])):
                col_bound = len(board[i]) - 1

                #The - 3 to the bound makes sure that i and/or j is in range to check a condition meaning if the base i or j
                # exceeds that then connect four cannot be True
                if i <= row_bound and j <= col_bound - 3:
                    if board[i][j] =="x" and board[i][j+1] =="x" and board[i][j+2] =="x" and board[i][j+3] =="x":
                        connect_four = True
                    elif board[i][j] =="o" and board[i][j+1] =="o" and board[i][j+2] =="o" and board[i][j+3] =="o":
                        connect_four = True
                        
                if i <= row_bound - 3 and j <= col_bound:
                    if board[i][j] =="x" and board[i+1][j] =="x" and board[i+2][j] =="x" and board[i+3][j] =="x":
                        connect_four = True
                    elif board[i][j] =="o" and board[i+1][j] =="o" and board[i+2][j] =="o" and board[i+3][j] =="o":
                        connect_four = True
                
                if i + 3 <= row_bound  and j + 3 <= col_bound:    
                    if board[i][j] =="x" and board[i+1][j+1] =="x" and board[i+2][j+2] =="x" and board[i+3][j+3] =="x":
                        connect_four = True                        
                    elif board[i][j] =="o" and board[i+1][j+1] =="o" and board[i+2][j+2] =="o" and board[i+3][j+3] =="o":
                        connect_four = True
                        
                if i + 3 <= row_bound and j <= col_bound:
                    if board[i][j] =="x" and board[i+1][j-1] =="x" and board[i+2][j-2] =="x" and board[i+3][j-3] =="x":
                        connect_four = True     
                    elif board[i][j] =="o" and board[i+1][j-1] =="o" and board[i+2][j-2] =="o" and board[i+3][j-3] =="o":
                        connect_four = True                        
        return connect_four

    def computer_player(self,board):
        #This function uses randint which allows the computer to generate two numbers to play the game
        computer_move = []

        #The + 1 to the row and col ensures that the move is in range of the board being used in the actually game
        for i in range(len(board)):
            row = len(board) -1
            row_input = randint(0,row)
            row_input += 1
            row_input = str(row_input)
            
            for j in range(len(board[i])):
                col = len(board[i]) - 1
                col_input = randint(0,col)
                col_input += 1
                col_input = str(col_input)
                
        computer_move.append(row_input)
        computer_move.append(col_input)            
        return computer_move
    
    def game_play(self):
        #The gameplay function calls all other functions into it to play the actual game and uses the class to call them 
        option = self.main_menu()

        while option != 3:
            board_file = []
            board = self.create_board(board_file)
            current_board = self.load_board(board)
            current_player = board[1]
            win = ""
            move = ""

            #Plays the 2 player game both games below are similar in most things and both have while loops that won't end till a player wins
            if option == 1:
                while win != True:
                    win = self.connect_four(current_board)
                    move = input("Player "+current_player+" What move do you want to make?  Answer as row (vertical) column (horizontal) or save game or load game: ")
                    move = move.lower()

                    #The save game function is used and to redisplay the cucrent game that was saved the show_saved_board function is called
                    if move =="save game":
                        save = self.save_board(current_board,current_player)
                        saved_file = self.show_saved_board(save)
                        current_board = self.load_board(saved_file)
                        
                    elif move =="load game":
                        make_board = []
                        board = self.create_board(make_board)
                        current_board = self.load_board(board)
                        current_player = board[1]
    
                    elif win == False:
                        valid = self.valid_move(current_board,move,current_player)
                        if valid[1] == True:
                            current_player = self.turn_flow(current_player)

                            #The other player had to be established because the winner is the player who went previous to the win happening
                            if current_player == self.player_1:
                                other_player = self.player_2
                            else:
                                other_player = self.player_1

                            win = self.connect_four(current_board)
                            if win == True:
                                print("The winner is player",other_player)                              
                        current_board = self.load_board(valid[0])
                #Returns the game to the main menu after it ends instead of exitting the file    
                option = self.main_menu()
           
            #The following code is the user playing aganist the computer the reason the connect four and turn flow functions as well as others are called twice
            # is because the system most acount for the player winning or the computer wininning
            elif option ==2:
                player_one_wins = False
                while win != True:
                    win = self.connect_four(current_board)
                    move = input("Player "+current_player+" What move do you want to make?  Answer as row (vertical) column (horizontal) or save game or load game: ")
                    move = move.lower()
                    
                    if move =="save game":
                        save = self.save_board(current_board,current_player)
                        saved_file = self.show_saved_board(save)
                        current_board = self.load_board(saved_file)

                    elif move =="load game":
                        make_board = []
                        board = self.create_board(board)
                        current_board = self.load_board(board)
                        current_player = board[1]

                    #Both the player and computers move most be valid, the turn must change each time they go, and a win must be checked multiple times
                    elif win == False:
                        valid = self.valid_move(current_board,move,current_player)
                        win = self.connect_four(current_board)

                        while valid[1] == False:
                            move = input("Player "+current_player+" What move do you want to make?  Answer as row (vertical) column (horizontal) or save game or load game: ")
                            valid = self.valid_move(current_board,move,current_player)
                            win = self.connect_four(current_board)
                                                    
                        if win == True:
                            print("The winner is player",current_player)
                            player_one_wins = True

                        current_player = self.turn_flow(current_player)
                        current_board = self.load_board(valid[0])

                        #The comp_move makes the two digits the computer returns into a string that looks like "row" "col" so that it can be read into valid move
                        if player_one_wins == False:
                            play = self.computer_player(current_board)
                            comp_move = " ".join(play)
                            valid = self.valid_move(current_board,move,current_player)

                            while valid[1] == False:
                                play = self.computer_player(current_board)
                                comp_move = " ".join(play)
                                valid = self.valid_move(current_board,comp_move,current_player)
                                
                            win = self.connect_four(current_board)
                            if win == True and player_one_wins == False:
                                print("The winner is player",current_player)

                            current_player = self.turn_flow(current_player)
                            current_board = self.load_board(valid[0])                                                          
                option = self.main_menu()
        
        if option == 3:
            print("Exiting game")
            
if __name__=="__main__":
    #Calls the class and sets it to the game_play function which allows game play
    #to read in other functions using self.function()
    game = AdjoinTheSpheres()
    game.game_play()
