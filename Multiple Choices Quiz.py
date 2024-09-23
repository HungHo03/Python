#FOR PROJECT
print ("Welcome to a Juan Gilbert Quiz!")
print ("Let's start!")
def multiple_choice_questions ():
    point = 0

    #Question 1
    print ("1. What is Juan Gilbert’s birthday?")
    print ("a. February 27, 1969")
    print ("b. February 17, 1969")
    print ("c. February 20, 1969")
    print ("d. February 9, 1969")

    choice1 = input ("Use only one letter, pick one of the following choices: ")
    if choice1 == "a" or choice1 == "A" :
        point += 1
        print ("Correct! :)")
    else:
        point += 0
        print ("Incorrect :(")

    #Question 2
    print ("2. Which university did Juan Gilbert graduate from?")
    print ("a. Miami University")
    print ("b. University of California San Diego")
    print ("c. University of Michigan")
    print ("d. University of Cincinnati")

    choice2 = input ("Use only one letter, pick one of the following choices: ")
    if choice2 == "a" or choice2 == "A":
        point += 1
        print ("Correct! :)")
    else:
        point += 0
        print ("Incorrect :(")

    #Question 3
    print ("3. From university did he attend, for his graduate program, to obtain his master of science degree in computer science?")
    print ("a. Miami University")
    print ("b. University of California San Diego")
    print ("c. University of Michigan")
    print ("d. University of Cincinnati")

    choice3 = input ("Use only one letter, pick one of the following choices: ")
    if choice3 == "d" or choice3 == "D":
        point += 1
        print ("Correct! :)")
    else:
        point += 0
        print ("Incorrect :(")

    #Question 4
    print ("4. What was Juan Gilbert’s major for his 4 years as an undergraduate?")
    print ("a. Chemistry")
    print ("b. Computer science")
    print ("c. Systems analysis")
    print ("d. Data analysis")

    choice4 = input ("Use only one letter, pick one of the following choices: ")
    if choice4 == "c" or choice4 == "C":
        point += 1
        print ("Correct! :)")
    else:
        point += 0
        print ("Incorrect :(")

    #Question 5
    print ("5. Where does Juan Gilbert teach now?")
    print ("a. University of Cincinnati")
    print ("b. University of Florida")
    print ("c. University of California, Berkeley")
    print ("d. He does not teach")

    choice5 = input ("Use only one letter, pick one of the following choices: ")
    if choice5 == "b" or choice5 == "B":
        point += 1
        print ("Correct! :)")
    else:
        point += 0
        print ("Incorrect :(")
    

    print("Game Over! Your final score is:", point)
    total(point)



def total(point):
    if point == 5:
        print ("You got 5/5! You rock!")
    elif point == 4:
        print ("You got 4/5! Almost! One more time!")
    elif point == 3:
        print ("You got 3/5! Close! Try again!")
    elif point == 2:
        print ("You got 2/5. Better luck next time!")
    elif point == 1:
        print ("You got 1/5. That's tough")
    else:
        print ("You got 0/5...") 

multiple_choice_questions()

retry = "yes"        
while retry == "yes":
    point = 0
    retry = input("Try again? Enter Yes or No: ")
    if retry == "Yes" or retry == "yes" or retry == "YES":
        multiple_choice_questions()
    else:
        print("Thanks for playing! Have a great day!")
        
