import random

def computer_choice():
    choices = ['r', 'p', 's']
    return random.choice(choices)

def play_again():
    answer = None
    while answer not in ('yes', 'y', 'no', 'n'):
        answer = input('Would you like to play again? y/n')
        if answer == 'yes' or answer == 'y':
            play_game()
        else:
            pass
    
def play_game():
    comp_choice = computer_choice()
    possible_choices = ['r', 'p', 's', 'rock', 'paper', 'scissors']
    game = True
    choice_dict = {'r':'rock', 'p':'paper', 's':'scissors'}

    while game is True:
        player_choice = input('What is your choice, rock (r), paper (p) or scissors (s)?').lower()
        if player_choice in possible_choices:
            player_choice = player_choice[0]
            game = False
            if player_choice == comp_choice:
                print('It is a tie! Both of you chose ' + choice_dict[player_choice] + '.')
            elif player_choice == 's' and comp_choice == 'p':
                print('Well done, you have won! Your choice was ' + choice_dict[player_choice] + ' and the computer chose ' + choice_dict[comp_choice] + '.')
            elif player_choice == 'p' and comp_choice == 'r':
                print('Well done, you have won! Your choice was ' + choice_dict[player_choice] + ' and the computer chose ' + choice_dict[comp_choice] + '.')
            elif player_choice == 'r' and comp_choice == 's':
                print('Well done, you have won! Your choice was ' + choice_dict[player_choice] + ' and the computer chose ' + choice_dict[comp_choice] + '.')
            else:
                print('Sorry, you have lost. Your choice was ' + choice_dict[player_choice] + ' and the computer chose ' + choice_dict[comp_choice] + '.')
        else:
            print('Sorry, your choice is not one of the possible choices, at least not for this game.')
            
    play_again()

play_game()
