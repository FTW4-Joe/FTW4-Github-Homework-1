#Asking player's name
 player_name = input("Please tell me your name: ").title()


#Storing player_name
print("Hi there "+ player_name +"! Welcome to Movie Trivia.\n======>>>Let's get started!<<======")


correct_score = 0  #Storing points for each correct answer


#Questions and Choices
quiz_1 = input(""""What is the highest-grossing film of all time without taking inflation into account?
A. Titanic 
B. Avengers: Endgame
C. Avatar
D. Star Wars: The Force Awakens
>>>> """).upper()

quiz_2 = input("""Which actor or actress is killed off in the opening scene of the movie Scream? 
A. Courtney Cox
B. Neve Campbell
C. Drew Barrymore
D. Rose McGowan
>>>> """).upper()

quiz_3 = input(""""Which film did Steven Spielberg win his first Oscar for Best Director?
A. Jaws
B. Catch Me If You Can
C. E.T.
D. Schindler’s List
>>>> """).upper()

quiz_4 = input(""""Which film won the first Academy Award for Best Picture?
A. All Quiet on the Western Front
B. Sunrise
C. Wings
D. Metropolis
>>>> """).upper()

quiz_5 = input(""""What is the name of Quint’s shark-hunting boat in Jaws?
A. The Whale
B. The Orca
C. The Dolphin
D. The Shark
>>>> """).upper()


#Logic Walkthrough - Storing points to correct_score variable
print(quiz_1)
if quiz_1 == "B":
    correct_score +=1
    print("correct!")
else:
    correct_score +=0
    print("wrong!")

print(quiz_2)
if quiz_2 == "C":
    correct_score +=1
    print("correct!")
else:
    correct_score +=0
    print("wrong!")

print(quiz_3)
if quiz_3 == "D":
    correct_score +=1
    print("correct!")
else:
    correct_score +=0
    print("wrong!")

print(quiz_4)
if quiz_4 == "C":
    correct_score +=1
    print("correct!")
else:
    correct_score +=0
    print("wrong!")

print(quiz_5)
if quiz_5 == "B":
    correct_score +=1
    print("correct!")
else:
    correct_score +=0
    print("wrong!")


#Score Result
print("=========>>>SCORE RESULTS<<<=========")
if correct_score == 5:
    print("WOW! Nice job! You got " + str(correct_score) +" out of 5 correct answers")
elif correct_score < 5:
    print("Keep on practicing pal! You got " + str(correct_score) +" out of 5 correct answers")