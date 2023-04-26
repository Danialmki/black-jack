from random import randint
import pygame
def main():
    random1 = randint(1, 11)
    random2 = randint(1, 11)
    random_P1 = randint(1, 11)
    random_P2 = randint(1, 11)
    player_sum = random_P1 + random_P2
    computer_sum = random2 + random1

    print(f"computer card => {random1}")
    print( "player cards ==>", random_P1, "  ", random_P2)
    while True:
        if computer_sum < 17:
            new_ran = randint(1, 11)
            computer_sum = computer_sum + new_ran
          #  print("computer new card", new_ran)
            if computer_sum > 17 and computer_sum < 21:
                continue
            if computer_sum > 21:
                print("computer lost, YOU WON")
                print(computer_sum)




        while True:
            new_card = randint(1, 11)
            if random_P1 + random_P2 > 21:
                print("you LOST")

            answer = input("do you want another card ? YES/NO")
            answer = answer.upper()
            if answer == "YES":
                player_sum = player_sum + new_card
                print(f"new card: {new_card}")
                print(f" players sum = {player_sum}")
            elif new_card + player_sum > 21:
                print("you lost")
                exit()

            if answer == "NO":
                player_sum = player_sum
                print(player_sum)
                exit()




            if computer_sum >= player_sum:
                print("computer won")
                print(computer_sum)
            else:
                print("player won")











if __name__ == "__main__":
    main()


#