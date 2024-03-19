import time
from Character import player
import sys


def attack_dragon(player):
    time.sleep(2)
    required_level = 7
    if player.level >= required_level:
        attack_minions_input = input("Do you want to proceed with attacking the dragon (yes/no) ")
        if attack_minions_input == "yes":
            print("You and the team of men attack, the dragon")
            time.sleep(1)
            print("some of the men with you perish to the fire from the dragon")
            time.sleep(1)
            print("Youself, barely makes it alive, with cuts and bruises everything,"
                  " you manage to cast a spell vanquishing the dragon")
            return True
        else:
            print("You decided to not attack")
            return False
    else:
        print(f"With reality setting in that taking the dragon head on will be suicide")
        time.sleep(2)
        print(f"the team of men decide it is best to sacrifice themselves distracting "
              f"the dragon giving you a chance for you to chase the dragon lord")
        time.sleep(2)
        repair_input = input("Do you chase the dargon lord? (yes/no)")
        if repair_input == "yes":
            time.sleep(2)
            print("The men valiantly and bravely throw themselves at the dragon, "
                  "sacrificing their lives to give you the chance to chase the dragon lord")
            return True
        else:
            print("You decide that you are not leaving the men behind, "
                  "however the dragon is just too powerful, killing you and your team of men")
            print("Game over.")
            sys.exit()


def run(player):
    print("--- Chapter 3---")
    print("You have defeated the minions, all that is left is the dragon lord and his dragon")
    time.sleep(2)
    print("You begin the trek up the volcano, where the dragon protects the base of the entrance")
    time.sleep(7)
    print("You can take this opportunity to attack the dragon head on")
    time.sleep(2)
    print("or come up with another plan")

    while True:
        print("\nWhat do you do?")
        print(f"Your current level is: {player.level}")
        print("1. Attack dragon (Make sure your level is high enough")
        print("2. Try to thin of another plan")

        choice = input("Enter your choice (1-2):")

        if choice == "1":
            return attack_dragon(player)
        elif choice == "2":
            print("You are able to sneak past the dragon, finally reaching the dragon lord")
            return True
        else:
            print("Invalid choice")

    chapter3_complete = check_completion()

    if chapter3_complete:
        return True
    else:
        return False

def check_completion():
    return True


run(player)