import random
def game():
    print("                                                     WELCOME TO GAME")
    name = input("Enter Your Name Player: ")
    user_score = 0
    play  = True

    # Step 1: Read previous high score
    with open("High_Score.txt", "r") as hs:
        lines = hs.readlines()
    # The score line looks like "Player's Score: 200"
    for line in lines:
        if "Score" in line:
            high_score = int(line.split(":")[1].strip())

    # Step 2: Game loop
    while play:
        computer_choice = random.choice(["Rock","Paper","Scissor"])
        print("Please Chosse from any one of these.\n1)Rock\n2)Paper\n3)Scissor")
        user_choice = input("Enter Your Choice: ").capitalize()
        print(f"You Choose: {user_choice}\nComputer Choose: {computer_choice}")

        if computer_choice == user_choice:
            print("IT'S A DRAW")
        elif computer_choice == "Rock":
            if user_choice == "Paper":
                print("YOU WON")
                user_score+=100
            elif user_choice == "Scissor":
                print("YOU LOSS")
                play = False
            else:
                print("Please Enter Valid Choice")
        
        elif computer_choice == "Paper":
            if user_choice == "Rock":
                print("You LOSS")
                play = False
            elif user_choice == "Scissor":
                print("YOU WON")
                user_score+=100
            else:
                print("Please Enter Valid Choice")

        elif computer_choice == "Scissor":
            if user_choice == "Paper":
                print("YOU LOSS")
                play = False
            elif user_choice == "Rock":
                print("YOU WON")
                user_score+=100
            else:
                print("Please Enter Valid Choice")
        if play:
            print("\nNEXT ROUND STARTS...")
        else:
            print("\nBetter luck next time!")
        print(f"Your Score is {user_score}")
    
    # Step 3: Compare and update high score
    if user_score > high_score:
        with open("High_Score.txt","w") as hs:
            print("🎉You beat The Previous Score")
            hs.write(f"Player's Name: {name}\nPlayer's Score: {user_score}")
    else:
        print(f"Current High Score is: {high_score}")


game()
