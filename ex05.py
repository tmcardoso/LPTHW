name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

convert_inches_to_centimeters = 2.54
convert_lbs_to_kilograms = 0.45359237

height_in_centimeters = height * convert_inches_to_centimeters
weight_in_kilograms = weight * convert_lbs_to_kilograms

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.",
    f"Or, he's {height_in_centimeters} centimeters tall.")
print(f"He's {weight} pounds heavy.",
    f"Or, he's {weight_in_kilograms} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
total_convert = age + height_in_centimeters + weight_in_kilograms
print(f"If I add {age}, {height}, and {weight} I get {total}.",
    f"Also, if I add {age}, {height_in_centimeters}",
    f"and {weight_in_kilograms}",
    f"I get {total_convert}.")
