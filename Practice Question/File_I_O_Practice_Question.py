# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< HARRY CODE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Q1

# poem_file = open("poem.txt")
# for i in poem_file:
#     if "Twinkle" in i:
#         print(True)
#     else:
#         print(False)
# poem_file.seek(0)
# print(poem_file.read())
# poem_file.close()

# Q2
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


# game()

# This shows the exact folder where Python is reading/writing files.
# import os
# print(os.getcwd())


# Q3

def cal_multiplication(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"tables/table_{n}","w") as f:
        f.write(table)

# for i in range(2,21):
#     cal_multiplication(i)

# Q4

# Step 1: Open the file and read its contents
# with open("donkey.txt") as old_file:
#     data = old_file.read()
# # Step 2: Replace the word
#     data = data.replace("donkey","#####")

# # Step 3: Write the modified data back to the file
# with open("donkey.txt","w") as new_file:
#     new_file.write(data)

#<<<<<<<<<<< Using a split function >>>>>>>>>>>>

# with open("split.txt","r",encoding="utf-8") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.split())



# Q5

# censored_list = ["bullshit","damn","hell","asshole","fucking","cracked"]

# Step 1:  Read the content of the file
# with open("log_1.txt") as file:
#     content = file.read()

# Step 2:  Replace all censored words
# for censored_word in censored_list:
#     if censored_word in content:
#         content = content.replace(censored_word,"*****")

# Step 3:  Write the cleaned text back to the file
# with open("log_1.txt","w") as new_file:
#         new_file.write(content)


# Q6

# with open("log_2.txt") as file:
#     contents = file.read()
#     if "Python" in contents:
#         print(True)
#     else:
#         print(False)


# Q7

# line_no = 1
# Step 1: Convert the files into lines format .
# with open("log_2.txt") as file:
#     lines = file.readlines()

# Step 2: finding the word "Pyhton" with loop of lines.
# for line in lines:
#     if "Python" in line:
#         print(f"Python found in {line_no}")
#     line_no+=1

# Q8

# with open("this_text_1.txt") as file:
#     file_content = file.read()

# with open("this_text_2.txt","w") as file_copy:
#     file_copy.write(file_content)

# Q9

# with open("this_text_1.txt") as file_1:
#     file_content_1 = file_1.read()

# with open("this_text_2.txt") as file_2:
#     file_content_2 = file_2.read()

# if file_content_1 == file_content_2:
#     print(True)
# else:
#     print(False)

# Q10

# with open("deleting_file.txt","w") as df:
#     df.write("")
    

# Q11    

# import os
# os.rename("renamed_by_ python.txt","renaming_by_ python.txt")
