import time
import random

print("Created by Adil")

# Game messages
loose = "The computer wins!"
win = "You win!"
lives = 5
score = 0
drew = 0
computer_lives = 7

# --- LOGIN SECTION ---
password_list = []

while True:
    print("To begin, fill in the below info.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Read account data
    with open("accounts.txt", "r") as searchfile:
        for line in searchfile:
            password_list.append(line.strip())

    # Check if both username and password exist
    if username in password_list and password in password_list:
        print("Access Granted")
        time.sleep(0.5)
        print("loading.")
        time.sleep(0.5)
        print("loading..")
        time.sleep(0.5)
        print("loading...")
        time.sleep(0.5)

        # --- START MENU ---
        print("Welcome", username + "!")
        print("-------------------------------------------------")
        print("| 🤘 ROCK     |     ✋ PAPER     |     ✂ SCISSORS |")
        print("-------------------------------------------------")
        print("Live Rules:")
        print("You start with 5 lives")
        print("If you win you get an extra life.")
        print("If you lose you lose a life.")
        print("If you draw, the lives stay the same.")
        print("-------------------------------------------------")
        print("To see a list of rules, type 'rules'")
        print("To see your lives, type 'display lives'")
        print("To see your score, type 'display score'")
        print("To see draws, type 'display draws'")
        print("-------------------------------------------------")
        print("At any point, type 'exit' to leave the game.")
        print("-------------------------------------------------")
        print("The computer has lives as well.")
        print("Can you beat the computer?")
        print("Good luck!!")
        print("-------------------------------------------------")

        # --- GAME LOOP ---
        while True:
            rps = input("Enter your choice (rock, paper, scissor): ").lower()
            computer = random.choice(["rock", "paper", "scissor"])

            # --- SYSTEM COMMANDS ---
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
                continue

            if rps == "display lives":
                print("-------------------------------------------------")
                print("Your Lives:", lives)
                print("-------------------------------------------------")
                continue

            if rps == "display score":
                print("-------------------------------------------------")
                print("Your Score:", score)
                print("-------------------------------------------------")
                continue

            if rps == "display draws":
                print("-------------------------------------------------")
                print("Your Draws:", drew)
                print("-------------------------------------------------")
                continue

            if rps == "exit":
                print("Thanks for playing!")
                break

            # --- GAME LOGIC ---
            if rps == "rock":
                if computer == "paper":
                    print("The computer chose", computer)
                    print(loose)
                    lives -= 1
                elif computer == "scissor":
                    print("The computer chose", computer)
                    print(win)
                    score += 1
                    lives += 1
                else:
                    print("The computer chose", computer)
                    print("It's a draw!")
                    drew += 1

            elif rps == "paper":
                if computer == "rock":
                    print("The computer chose", computer)
                    print(win)
                    score += 1
                    lives += 1
                elif computer == "scissor":
                    print("The computer chose", computer)
                    print(loose)
                    lives -= 1
                else:
                    print("The computer chose", computer)
                    print("It's a draw!")
                    drew += 1

            elif rps == "scissor":
                if computer == "rock":
                    print("The computer chose", computer)
                    print(loose)
                    lives -= 1
                elif computer == "paper":
                    print("The computer chose", computer)
                    print(win)
                    score += 1
                    lives += 1
                else:
                    print("The computer chose", computer)
                    print("It's a draw!")
                    drew += 1

            else:
                print("Invalid input. Type rock, paper, or scissor.")
                continue

            # --- CHECK GAME STATUS ---
            if lives <= 0:
                print("-------------------------------------------------")
                print("You ran out of lives!")
                print("Your final score:", score)
                print("Your final draws:", drew)
                print("-------------------------------------------------")
                input("Press Enter to exit the game...")
                exit()

            if computer_lives <= 0:
                print("-------------------------------------------------")
                print("The computer ran out of lives. You won!")
                print("Your final score:", score)
                print("Your final draws:", drew)
                print("-------------------------------------------------")
                input("Press Enter to exit the game...")
                exit()

    else:
        print("Your username or password is incorrect.")
        print("---------------------------------------")
