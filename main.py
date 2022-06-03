from random import choice
play_again=True
def game():
    game_in_progress=True
    print('Welcome to Rock,Paper,Scissors Game By Temple')
    print('**************************************************')
    print('INSTRUCTIONS/HOW TO PLAY')
    print('To Choose Rock Press R,Scissors Press S, Paper Press P')
    identifiers= {
        "r":"Rock",
        "s":"Scissors",
        "p":"Paper"
    }
    while game_in_progress:
         computer_choice= choice(['r','s','p'])
         player_select= input('Choose from the options: [R,S,P]\n')
         player_select=player_select.lower()
         if player_select not in ['r','s','p']:
             print('invalid option ' + player_select + " Please input the Right Option")
             continue
         else:
            if(player_select == computer_choice):
                print(f"Player Move ({identifiers[player_select]}) : CPU Move ({identifiers[computer_choice]})") 
                print("its a Tie Please Try Again")
                continue  
            elif computer_choice=="r" and player_select=="s" or computer_choice=="p" and player_select=="r" or computer_choice=="s" and player_select=="p" :
                print("Computer Wins")   
                game_in_progress=False 
            else:
                print("Player Wins")
                game_in_progress=False
            print(f"Player Move ({identifiers[player_select]}) : CPU Move ({identifiers[computer_choice]})") 
            print("Thanks For Playing My Game") 
game()

""" while play_again:
    chosen = input("Would you Like To Play Again: y/n \n")
    if chosen=="y":
        game()
    elif chosen == "n":
        play_again=False """

    

