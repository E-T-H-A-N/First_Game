
def play_game():
    print("played")
    player_name = input("Whats your name? ")
    print("hello", player_name)
    if player_name.lower() == "ethan":
        print("Hey thats my name!")
    print("")
    print("")
    game_choice = input("Are you ready to start this game?! ")
    if game_choice.lower() in ["yes", "yah", "yee", "of course", "yes i do"]:
        print("Okay!")
    if game_choice.lower() == "no":
        quit()



def title_screen():
    print("####################")
    print("#     Welcome      #")
    print("#       to         #")
    print("#    Neat Ville    #")
    print("#     -play        #")
    print("#     -options     #")
    print("#     Have Fun!    #")
    print("####################")

play_choice = ""

def input_choice():
    play_choice=input("> ")
    if play_choice.lower() == "play":
        play_game()
    if play_choice.lower() != "play":
        print("Enter Correct Command")
        input_choice()

title_screen()
input_choice()
