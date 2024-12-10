import sys
import random


def guess_number(name= 'playerOne'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins


        playerchoice = input (f"\n{name},guess which number i'am thinking of...1,2 or 3.\n\n")

        if playerchoice not in ["1","2","3"]:
            print(f"\n Please enter 1,2 or 3.")
            return play_guess_number()
        
        computerchoice = random.choice("123")

        print(f"\n {name},you chose {playerchoice}.")
        print(f"\nI was thinking about the number {computerchoice}.\n")


        player = int(playerchoice)

        computer = int(computerchoice)


        def decide_winner(player,computer):
            nonlocal name  # why do the nonlocal name and player_wins
            nonlocal player_wins


            if player == computer :
                player_wins +=1
                return f"{name}, you win!"
            else:
                return f"\n sorry,{name},better luck next time.😉"
            
        game_result = decide_winner(player,computer)
        print(game_result)


        nonlocal game_count
        game_count +=1


        print(f"\nGame count:{game_count} ")
        print(f"\n{name}'s wins:{player_wins}")
        print(f"\n Your winning percentage: {player_wins/game_count:.2%}")


        print(f"\nplay again,{name}? ")

        while True:
            playagain = input("\n Y for yes or /n Q to quit/n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break

        if playagain.lower()=="y":
            return play_guess_number()
        else:
            print("/n🎉🙌")
            print("Thankyou for playing!/n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!")
            else:
                return 
            
        return play_guess_number
    
if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personalized game experience."
    )

    parser.add_argument('-n','--name',metavar='name', required = True, help = 'the name of the person playing the game.')

    args = parser.parse_args()

guess_my_number = guess_number(args.name)
guess_number()








