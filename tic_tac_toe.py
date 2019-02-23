'''
Created on Feb 23, 2019

@author: Shubham
'''
try:
    def tic_tac_toe():
        player="X" 
        theBoard={'top-L':" ","top-M":" ","top-R": " ","mid-L":" ","mid-M":" ","mid-R":" ","low-L":" ","low-M":" ","low-R":" "}
        def print_board():  
            print("\t"+theBoard['top-L']+"|"+theBoard['top-M']+"|"+theBoard['top-R'])
            print("\t"+"-"+"+"+"-"+"+"+"-")
            print("\t"+theBoard['mid-L']+"|"+theBoard['mid-M']+"|"+theBoard['mid-R'])
            print("\t"+"-"+"+"+"-"+"+"+"-")
            print("\t"+theBoard['low-L']+"|"+theBoard['low-M']+"|"+theBoard['low-R'])
        
        def players_turn(player):
            print("Player " +str(player)+" please select one place")
        def change_player(current_player):
            if(current_player=="X"):
                return "O"
            return "X"
        def place_empty(place):
            if(theBoard[place]==" "):
                return True
            return False
        def winner_checker(player):
            if(theBoard['top-L']==theBoard['top-M']==theBoard['top-R']==player or \
               theBoard['mid-L']==theBoard['mid-M']==theBoard['mid-R']==player or \
               theBoard['low-L']==theBoard['low-M']==theBoard['low-R']==player  or \
               theBoard['top-L']==theBoard['mid-M']==theBoard['low-R']==player or \
               theBoard['low-L']==theBoard['mid-M']==theBoard['top-R']==player):
                    print(player + " is winner")
                    return True
        def starter_print():
            print("-----Welcome to Tic Tac Toe-----")
            print("This game has two Player X and O")
            print_board()
            players_turn("X")          
                    
        starter_print()            
        while(True):
            
            input_by_user=input()
            if(place_empty(input_by_user)):
                theBoard[input_by_user]=player
                print_board()
                if(winner_checker(player)):
                    print("------------------------------------------")
                    break
                player=change_player(player)
                players_turn(player)
            else:
                print("Place already occupied ,Please Try another one")
                continue
        
        
           
        starter_print()  
    tic_tac_toe() 
except :
    print("some error")      
