# import sys module
from sys import argv

# command-line arguments passed to the script
# script, filename = argv

# open file and stores in txt variable
# txt = open(filename)

# prints filename
# print(f"Here's your file {filename}:")
print("Type the filename:")
filename = input("> ")

txt = open(filename)
# prints the content of the opened file stored in txt variable
# .read() is a function that reads a specific opened file
print(txt.read())

# close file
txt.close()

# prints a question
# print("Type the filename again:")
# prints "> " and wait for the user's answer
# stores the filemane in file_again variable
# file_again = input("> ")

# open file and stores in txt_again variable
# txt_again = open(file_again)

# prints the content of the opened file stored in txt_again variable
# .read() is a function that reads a specific opened file
# print(txt_again.read())
