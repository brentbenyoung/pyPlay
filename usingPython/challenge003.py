# Write a program to find out whether "Some text" is the same as "some text", whether -4 is less than -6, and wheter the string "part" is in the string "party!!!1". Then write a program to ask a person's age, and tell them wheter it is a valid age or not. For example -12 and 312 are not valid ages, but 0; 12; and 89 are valid ages


#Does "Some text" == "some text"
print("Is 'Some text' the same as 'some text'?")
print("Some text" == "some text")

#Is -4 less the -6
print("Is -4 less than -6?")
print(-4 < -6)

#Is the word 'part' in the string 'party!!!1'
print("Is the word 'part' in the string 'party!!!1'")
print('part' in 'party!!!1')



#Write a program to ask a person's age, and tell them wheter it is a valid age or not. For example -12 and 312 are not valid ages, but 0; 12; and 89 are valid ages.

age = input("Please enter your age:")
print(age > -1) and (age < 120)
