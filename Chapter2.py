import time
from Character import player


def check_completion():
    return True


def help_villagers(player):
    time.sleep(2)
    print("You see that this village has also been destroyed")
    time.sleep(3)
    print("You search around and help clean rubble and dig for survivors")
    print("You have helped as much as you could and the villagers are thankful")
    player.add_level(1)


def rally_soldiers(player):
    time.sleep(2)
    print("You find a few men are still capable of fighting")
    time.sleep(1)
    print("With revenge set in their hearts for the loss of their loved ones and homes")
    time.sleep(2)
    print("They ask if they can join you in your quest to find your sister and take down the dragon lord")
    time.sleep(3)
    print("You accept and you now have a small team")
    player.add_level(1)


def talk_to_villagers(player):
    time.sleep(2)
    print("You ask the survivors what happened")
    time.sleep(3)
    print("The dragon lord came through, destroying everything in its path, "
          "they took a few other women prisoners and your sister was spotted among them, you are told"
          "him and his minions went south.")
    player.add_level(1)


def smithing(player):
    time.sleep(2)
    required_level = 5
    if player.level >= required_level:
        upgrade_armor = input(
            f"You have helped enough villagers, that the local blacksmith"
            f" wants to upgrade your armor and weapon, Do you accept? (yes/no) ")
        if upgrade_armor == "yes":
            print("You are now equipped to continue your "
                  "journey, with new allies and upgraded weaponry, you travel south")
            return True
        else:
            print("You decide to keep looking around")
            return False
    else:
        print(f"The blacksmith is busy tending to the survivors, try helping them too")
        return False


def run(player):
    print("--- Chapter 2 ---")
    time.sleep(2)
    print("As you traveled south, in the distance by the horizon you see a billow of smoke ")
    time.sleep(2)
    print("As you rush toward the smoke, you noticed that "
          "this was a nearby village that was also attacked by the dragon lord")
    time.sleep(7)
    print("You run into the village to see what happened")
    time.sleep(2)
    print("You see that the majority of the village was destroyed, there are survivors however")

    while True:
        print("\nWhat do you do?")
        print(f"Your current level is: {player.level}")
        print("1. Help the villagers")
        print("2. Rally surviving men")
        print("3. Talk to the villagers")
        print("4. Ask the blacksmith for help upgrading your armor")

        choice = input("Enter your choice (1-4):")

        if choice == "1":
            help_villagers(player)
        elif choice == "2":
            rally_soldiers(player)
        elif choice == "3":
            talk_to_villagers(player)
        elif choice == "4":
            if smithing(player):
                break
        else:
            print("Invalid choice")

    chapter2_complete = check_completion()

    if chapter2_complete:
        return True
    else:
        return False


def check_completion():
    return True


run(player)
