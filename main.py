print("created by adil")
loose = ("the computer wins")
Win = ("you win")
lives = 5
score = 0
drew = 0
computer_lives = 7
while True:
    print("To begin fill in the below info.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    searchfile = open("accounts.csv", "r")
    for line in searchfile:
        if username and password in line:
          print("Access Granted")
          print("-------------------------------------------------")
          print("| 🤘 ROCK     |     ✋ PAPER     |     ✂ SCISSORS |")
          print("-------------------------------------------------")
          print("-------------------------------------------------")
          print("Live Rules:")
          print("If you win you get a extra live.")
          print("If you lose you lose a live.")
          print("If you draw the lives stay the same.")
          print("-------------------------------------------------")
          print("MAKE SURE YOU DONT USE CAPITAL LETTERS")
          print("-------------------------------------------------")
          print("To see a list of rules type rules")
          print("-------------------------------------------------")
          print("At any point type exit to leave the game")
          print("-------------------------------------------------")
          print("The computer has lives as well.")
          print("Can you beat the computer?")
          print("Good luck!!")
          print("-------------------------------------------------")
          while True:
            rps = input("Enter your choice (rock, paper, scissor): ")
            import random
            computer = ("rock", "paper", "scissor")
            computer = random.choice(computer)
            # rock if statement
            if rps == "rock" and computer == "paper":
              print("The computer choice",computer)
              print("")
              print(loose)
              print("")
              print("")
              lives -= 1
            if rps == "rock" and computer == "scissor":
              print("The computer choice",computer)
              print("")
              print(Win)
              print("")
              print("")
              score += 1
            # paper if statement
            if rps == "paper" and computer == "rock":
              print("The computer choice",computer)
              print("")
              print(loose)
              print("")
              print("")
              lives += 1
            if rps == "paper" and computer == "scissor":
              print("The computer choice",computer)
              print("")
              print(Win)
              print("")
              print("")
              score -= 1
            # scissor if statement
            if rps == "scissor" and computer == "rock":
              print("The computer choice",computer)
              print("")
              print(loose)
              print("")
              print("")
              lives -= 1
            if rps == "scissor" and computer == "paper":
              print("The computer choice",computer)
              print("")
              print(Win)
              print("")
              print("")
              score += 1
            # duplicates
            if rps == computer:
              print("The computer choice",computer)
              print("")
              print("It's a draw!")
              print("")
              print("")
              drew += 1
            # system
            if rps == "rules":
              print("-------------------------------------------------")
              print("Game Rules:")
              print("-------------------------------------------------")
              print("1. Rock beats Scissors")
              print("2. Rock loses to Paper")
              print("3. Paper beats Rock")
              print("4. Paper loses to Scissors")
              print("5. Scissors beats Paper")
              print("6. Scissors loses to Rock")
              print("-------------------------------------------------")
            # if the user wants to see their lives
            if rps == "display lives":
              print("-------------------------------------------------")
              print("Your Lives:", lives)
              print("-------------------------------------------------")
            # if the user wants to see the score
            if rps == "display score":
              print("-------------------------------------------------")
              print("Your Score:", score)
              print("-------------------------------------------------")
            # if the user wants to see the draws
            if rps == "display draws":
              print("-------------------------------------------------")
              print("Your Draws:", drew)
              print("-------------------------------------------------")
            # lives
            if lives == 0 or rps == "test":
              print("Thanks for playing")
              print("You ran out of lives")
              print("Your final score:", score)
              print("Your final draws:", drew)
              stop = input("Press Enter to stop playing...")
              import time
              time.sleep(3)
            if computer_lives == 0:
              print("Thanks for playing")
              print("The computer ran out of lives,You won!")
              print("Your score:", score)
              print("Your draws:", drew)
              stop = input("Press Enter to stop playing...")
              import time
              time.sleep(900)
            #exit
            if rps == "exit":
              break
    else:
      print("Your username or password is incorrect.")
      print("---------------------------------------")
