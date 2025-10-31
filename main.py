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
