import time
from Character import player


def check_completion():
    return True


def help_villagers(player):
    time.sleep(1)
    print("You help the villages put out fires and rescue survivors")
    time.sleep(3)
    print("The villagers are safe, as a thank you they give you potions for your adventure to come")
    player.add_level(1)


def search_village(player):
    time.sleep(1)
    print("You look through the rubble")
    time.sleep(1)
    print("searching...")
    time.sleep(3)
    print("searching...")
    time.sleep(3)
    print("You find your magic staff")
    player.add_level(1)


def talk_to_villagers(player):
    time.sleep(1)
    print("You ask the survivors what happened")
    time.sleep(3)
    print("They tell you the dragon lord came through and destroyed everything,"
          " and took your sister prisoner, he went east.")
    player.add_level(1)


def travel(player):
    time.sleep(1)
    required_level = 4
    if player.level >= required_level:
        travel_option = input(
            f"You are now equipped to travel in search of your sister, do you want to proceed? (yes/no) ")
        if travel_option == "yes":
            print("With potions, your staff and knowledge of the the direction"
                  " the dragon lord when, you are now on your way, in a quest to find your sister")
            time.sleep(2)
            return True
        else:
            print("You decide to stick around")
            return False
    else:
        print(f"You are currently not properly equipped, try helping others")
        time.sleep(2)
        return False


def run(player):
    print("--- Chapter 1 ---")
    time.sleep(2)
    print("In the age of dragons, a million years ago, ")
    time.sleep(2)
    print("You, a young wizard from the town of towny, are thrown into a situation which calls for you to be brave ")
    time.sleep(7)
    print("Your town has been attacked by a dragon lord, his dragon destroyed"
          "\nmost of the town and the dragon lord took your sister ")
    time.sleep(4)
    print("You awaken, being knocked out by the destruction, you are not sure what happened")
    time.sleep(3)

    while True:
        print("\nWhat do you do?")
        print(f"Your current level is: {player.level}")
        print("1. Help the villagers")
        print("2. Search the rubble")
        print("3. Talk to the villagers")
        print("4. Head out in search of your sister")

        choice = input("Enter your choice (1-4):")

        if choice == "1":
            help_villagers(player)
        elif choice == "2":
            search_village(player)
        elif choice == "3":
            talk_to_villagers(player)
        elif choice == "4":
            if travel(player):
                break
        else:
            print("Invalid choice")
    chapter1_complete = check_completion()

    if chapter1_complete:
        return True
    else:
        return False


run(player)
