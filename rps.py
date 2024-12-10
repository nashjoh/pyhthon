import sys
import random # return  random numbers for computer choice here.
from enum import Enum
#ENUM is used to return the values of 1,2and 3 ie rock paper and scissors in the output here.

def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

                
        playerchoice = input(f"\n{name},please enter ....\n1 for rock,\n2 for paper or \n3 for scissors:\n\n")
        if playerchoice not in ["1","2","3"]:
            print(f"{name}, please enter 1,2 or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")# computer could choose any random number from 123
        computer = int(computerchoice)


        print (f"\n{name}, you chose { str(RPS(player)) .replace('RPS.','').title()}.")
        print (f"python chose { str(RPS(computer)).replace('RPS.','').title()}.\n")

        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
        
            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name}, You Win!🎉🐱‍🐉"
            elif player == 2 and computer == 1:
                player_wins +=1
                return f"{name}, You Win!🎉🐱‍🐉"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name}, You Win!🎉🐱‍🐉"
            elif player ==  computer:
                return"Its a tie!👀"
            else:
                python_wins +=1
                return f"Python win!'🐍🎉\n sorry, {name}...💔"
        game_result = decide_winner (player,computer)

        print(game_result)

        nonlocal game_count
        game_count +=1

        print(f"\n Game Count: { game_count}") 
        print(f"\n {name}'s wins: {player_wins}" )
        print(f"\n python_wins:  {python_wins}" )


        print(f"\nplay again,{name} ?")
        while True:
            playagain = input("\n Y for yes or \n Q for quit \n\n" )
            if playagain.lower()not in ["y","q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉👏 ")
            print("Thankyou for playing!\n")
            sys.exit(f"bye {name}!!!")

    return play_rps

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provide  personal game experience."
    )

    parser.add_argument(
        "-n","--name", metavar ="name",
        required = True,help = "the name of the person plaing the game ."
    )
    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()

