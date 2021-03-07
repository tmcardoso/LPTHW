# import sys module
from sys import argv

# command-line arguments passed to the script
script, user_name, age = argv
# prompt var to be shown to the user after a question is asked
prompt = '...' #'> '

# prints a statement
print(f"Hi {user_name} with {age} years old, I'm the {script} script.")
# prints another statement
print("I'd like to ask you a few questions.")
# prints a question
print(f"Do you like me {user_name}?")
# waits for the user's answer and stores in likes var
likes = input(prompt)

# prints another question
print(f"Where do you live {user_name}?")
# waits for the user's answer and stores in lives var
lives = input(prompt)

# prints last question
print("What kind of computer do you have?")
# waits for the user's answer and stores in computer var
computer = input(prompt)

# prints all the answers
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
