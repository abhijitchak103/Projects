import random

computer_options = ['rock', 'paper', 'scissor']

user_score = 0
computer_score = 0

flag = True
while flag:
    n = int(input("Please select an odd number for number of rounds.: "))

    for i in range(n):
        print(f"\nRound {i+1}:")
        user_choice = input("Choose your play, 'rock', 'paper' or 'scissor': ")
        computer_choice = random.choice(computer_options)
        print(f"You played: {user_choice} and Computer played: {computer_choice}")

        if user_choice == computer_choice:
            print("Round tie. 0 points to each")
        elif user_choice == 'rock':
            if computer_choice == 'paper':
                print("Computer wins the round. 1 point to Computer.")
                computer_score += 1
            else:
                print("You win the round. 1 point to you.")
                user_score += 1
        elif user_choice == 'paper':
            if computer_choice == 'scissor':
                print("Computer wins the round. 1 point to Computer.")
                computer_score += 1
            else:
                print("You win the round. 1 point to you.")
                user_score += 1
        elif user_choice == 'scissor':
            if computer_choice == 'rock':
                print("Computer wins the round. 1 point to Computer.")
                computer_score += 1
            else:
                print("You win the round. 1 point to you.")
                user_score += 1
        elif user_choice not in computer_options:
            print("Invalid response. Round goes to Computer.")

    if user_score > computer_score:
        print(f"\nCongratulations! You win. Your score: {user_score} and Computer score: {computer_score}")
    elif computer_score > user_score:
        print(f"\nSorry! You lose. Your score: {user_score} and Computer score: {computer_score}")
    else:    
        print(f"\nMatch ended in a tie. Your score: {user_score} and Computer score: {computer_score}")
    
    print("--------------------------------------------------------------------------------------------")

    continuity = input(f"Do you want to play another game? Press 1 to confirm and 0 to exit the game.\n")
    if continuity == '0':
        print(f"Match ended by User. Bye for now.\n")
        flag = False
    else:
        print("Starting another match in 3...2...1...")
        print("--------------------------------------------------------------------------------------------")
        continue
