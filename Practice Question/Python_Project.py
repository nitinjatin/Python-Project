import random
def game():
    print("                                                     WELCOME TO GAME")
    name = input("Enter Your Name Player: ")
    user_score = 0
    play  = True
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
        
        elif computer_choice == "Paper":
            if user_choice == "Rock":
                print("You LOSS")
                play = False
            elif user_choice == "Scissor":
                print("YOU WON")
                user_score+=100

        elif computer_choice == "Scissor":
            if user_choice == "Paper":
                print("YOU LOSS")
                play = False
            elif user_choice == "Rock":
                print("YOU WON")
                user_score+=100
        if play:
            print("\nYOU WON! NEXT ROUND STARTS...")
        else:
            print("\nBetter luck next time!")
        print(f"Your Score is {user_score}")
    

game()
