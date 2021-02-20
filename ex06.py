# Init var types_of_people and set it value equals to 10
types_of_people = 10
# Init var x and set value equals to a specific string
# plus the types_of_people var
x = f"There are {types_of_people} types of people."

# Init var binary
binary = "binary"
# Init var do_not
do_not = "don't"
# Init var y and set values equals do a specific string
# plus the two variables (binary and do_not)
# String is put inside a string (2 times)
y = f"Those who know {binary} and those who {do_not}."

# Prtins var x
print(x)
# Prints var y
print(y)

# Prints a string with var x
# String is put inside a string
print(f"I said: {x}")
# Prints a string with var y
# String is put inside a string
print(f"I also said: '{y}'")

# Init a boolean variable
hilarious = True
# Init joke_evaluation var as a string
joke_evaluation = "Isn't that joke so funny?! {}"

# Print joke evaluation var string plus boolear var (hilarious)
print(joke_evaluation.format(hilarious))

# Init var w as string
w = "This is the left side of..."
# Init var e as a string
e = "a string with a right side."

# Prints var w and e
print(w + e)
