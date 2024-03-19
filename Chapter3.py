import time
from Character import player
import sys


def attack_minions(player):
    time.sleep(2)
    print("As you reach the camp, the minions are unaware of your presence and you have the option to attack")
    required_level = 7
    if player.level >= required_level:
        attack_minions_input = input("Do you want to proceed with attacking (yes/no) ")
        if attack_minions_input == "yes":
            print("You and your team of men brutally defeated the minions")
            return True
        else:
            print("You decided to not attack")
            return False
    else:
        print(f"You might not be strong enough to overtake the minions during daylight")
        time.sleep(2)
        print(f"Do you want to repair your armor and sharpen your sword, while you prepare for an attack at night")
        time.sleep(2)
        repair_input = input("Would you rather wait for nightfall? (yes/no)")
        if repair_input == "yes":
            time.sleep(2)
            print("You and your team of men brutally defeated the minions under the cover of night")
            return True
        else:
            print("You proceeded with the attack, and you died")
            print("Game over.")
            sys.exit()


def run(player):
    print("--- Chapter 3---")
    print("With a team of angry soldiers, you start to catch up to the dragon lord and his minions ")
    time.sleep(2)
    print("You reach the outskirts of the camp and see they have 100s of minions sleeping")
    time.sleep(7)
    print("You can take this opportunity to attack")
    time.sleep(2)
    print("or you can wait to attack at night, gaining an upperhand")

    while True:
        print("\nWhat do you do?")
        print(f"Your current level is: {player.level}")
        print("1. Attack minions (Make sure your level is high enough")
        print("2. Wait for night fall")

        choice = input("Enter your choice (1-2):")

        if choice == "1":
            return attack_minions(player)
        elif choice == "2":
            print("You decided to wait for nightfall, and you slaughtered the minions")
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