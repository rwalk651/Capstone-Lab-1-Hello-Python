#Write a program that asks for your name and the month you were born in.
from datetime import date

user_name = input('What is your name?')

birth_month = input(str('Enter the month you were born in: '))

#A greeting to you, using your name
print(f'Hello, {user_name}!')

#A message with the number of letters in your name
letters_in_names = len(user_name)

print(f'You have {letters_in_names} letters in your name.')

#A 'Happy birthday month!' message if you were born in the current month
if birth_month == 'August':
    print('Happy birthday month!')
else:
    print()

today = date.today()
print(today)
this_month = today.month
print(this_month)

#Write a program that asks for the names of all of the classes you are taking this semester
#Save these class names in a list.
#Print all the items in the list, one per line.

classes = []

while True:
    class_name = input('Enter all of the classes you are taking this semester or enter nothing to stop: ')
    if class_name == '':
        break
    else:
        classes.append(class_name)

print(classes)


#Write a program that turns a sentence into camel case. The first word is lowercase, the rest of the words have
# their initial letter capitalized, and all of the words are joined together. For example, with the input
# "fOnt proCESSOR and ParsER", your program will output "fontProcessorAndParser".
#Optional extra question: print a warning message if the input will not produce a valid variable name. You don't
# need to be exhaustive in checking, but test for a few common issues, such as starting with a number, or containing invalid characters such as # or + or ".  Or, would it be easier to check that the name only contains valid characters?
#Test your program with different example inputs, and comment your code.

