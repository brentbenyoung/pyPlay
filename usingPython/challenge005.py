# B.O.B Ver.1

#ask a question
print("Hello human. I'm B.O.B. What is your name?")
#get the answer
input()
#ask another question
print("That's a lovely name.")
print("Is there anything you'd like to know?")
#get the answer
input()
#ask another question
print("I'm a computer, not a human. Did you like that information?");
#get the answer
input()
#Print goodbye
print("Goodbye.");


#Print a division between B.O.B. Ver.1 and B.O.B. Ver.2
print("______________________________________________________")



# Modify B.O.B. Ver.1 using if/else statements to react to the user's responses instead of just ignoring them. Assume the user will always answer yes or no.

# B.O.B. Ver.2

#Get users name
print("Hello human. I'm B.O.B(Ver.2). What is your name?")
name = input()
print("That's lovely name " + name + " ...")

#Ask user a question. If true print a B.O.B. fact and ask if the user liked the fact, if they did say thank you, if they didnt print that bob is sad. Else they didnt like the BOB fact then print that BOB is sad and end.
print("Say... would you like a B.O.B.(Ver.2) Fact™ ?")
answer = input()

if answer.lower() == "yes" or answer.lower() == "y":
    print("I'm a computer, not a human. Between just you and me this is my second iteration. I was rather lousy before... but don't tell anyone. Did you like that fact?")
    like = input()
    if like.lower() == "yes" or like.lower() == "y":
        print("OH GOOD! That makes me so happy to hear! We'll talk again soon. Bye-bye!")
    else:
        print("Oh...I'm so sorry to have bothered you. You may see yourself out now...")
else:
    print("Oh. Well then. Why are you bothering me? Leave me alone! Goodbye.")
