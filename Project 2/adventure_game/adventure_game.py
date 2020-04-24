#!/usr/bin/env python3
"""

"""
# import os, time and random module
import os
import time
import random


def play_the_game():
    """Main Menu.
    First main screen from the game.
    """
    clear_screen()
    print("=================================\n"
          "\nWelcome to Bona's Adventure Game\n "
          "\n=================================\n")
    time.sleep(2)
    item = []
    option = random.choice(["barn", "church", "cave",
                            "another town", "graveyard"])
    

    intro_game(item, option)
    main_field(item, option)
    

def clear_screen():
    """Clearing the screen.
    Clear the screen from all of text.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def typing_game(msg_to_print):
    """Pause between typing.
    Adding timer sleep for 1 second.
    """
    print(msg_to_print)
    time.sleep(1)


def intro_game(item, option):
    """Introduction in Game.
    First intro at the Game.
    """
    

    typing_game("You're an ordinary farmer with ordinary life "
                "One day, your partner captured by bandit.")
    typing_game("Rumor has it that your partnerd held in " + option + " or you heard so from villager ")
    typing_game("You have two option,")
    typing_game("Find and rescue your partner.\n")
    typing_game("Abandon your partner.\n")
    typing_game("Right now you realize you only have a dull dagger.\n")



def option_abandon(item, option):
    """Option to abandon your partner.
    Player select to abandon.
    """
    typing_game("\nYou choose to abandon your friend.")
    typing_game("\nsince then, you never heard of her again.")
    typing_game("\nYou realize that was a mistake .")          
    typing_game("\nBecause in the you realize, you rather die, than live lonely")
    play_again()


def option_rescue(item, option):
    """Option to rescue.
    Player selected rescue.
    """
    typing_game("\nYou have arrive in front " + option + ".")
    typing_game("\nYou check the door, and it's open ")           
    typing_game("\nIn front of you there is a red door and blue door")

   
    while True:
        choice2 = input("Choose Red Door (1)\nChoose Blue Door (2)\n")
                        
        if choice2 == "1":
            typing_game("\nYou choose red door "
                            "you come into armory room.")
            typing_game("\nin the armory lies Great Silver Sword "
                            "you decide to pick it up to change your dull dagger "
                            "attack.")
            typing_game("\nAfter you leave the armor room, King bandit have appear in front of you "
                            "with your new sword, there is nothing can defeated you")
            typing_game("\nYou have defeated king bandit and rescue your friend")
            play_again(1)
            break
        

        if choice2 == "2":
            typing_game("\nYou choose blue door. "
                        "\nYou come into dark room. "
                        "\nin the corner of the room, there is King bandir staring at you. "
                        "\nYou realize you have slim chance to defeated him, but you do it anyway. "
                        "followed.\n")
            play_again(item, option)
            break


def main_field(item, option):
    """Main Field.
    Field to choose door.
    """
    typing_game("Enter 1 to Rescue your partner.")
    typing_game("Enter 2 to Abandon your partner.")
    typing_game("Which door would you choose ?")

    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            option_rescue(item, option)
            break
        elif choice1 == "2":
            option_abandon(item, option)
            break


def play_again():
    """Re-Start Game.
    Question if want to play again or not.
    """
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        typing_game("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_the_game()
    elif again == "n":
        typing_game("\n\n\nThank you for playing this game!"
                    "\nI hope you enjoy!\n"
                    "See you next time.\n\n\n")
        clear_screen()
    else:
        play_again()


# Let's Play this Game
play_the_game()