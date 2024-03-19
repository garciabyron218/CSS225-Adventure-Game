import Chapter1
import Chapter2
import Chapter3
import Chapter4
from Character import player


def main(player):
    chapter1_completed = Chapter1.run(player)
    if chapter1_completed:
        print("\n--- Chapter 2 ---")
        chapter2_completed = Chapter2.run(player)

        if chapter2_completed:
            print("\n--- Chapter 3 ---")
            chapter3_completed = Chapter3.run(player)

            if not chapter3_completed:
                print("\n---Chapter 2 again ---")
                Chapter2.run(player)
            else:
                print("\n ---Chapter 4 ---")
                Chapter4.run(player)
        else:
            print("Chapter was not competed")
    else:
        print("Chapter was not competed")


if __name__ == "__main__":

    main(player)
