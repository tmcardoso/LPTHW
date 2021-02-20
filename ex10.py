tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

single_quote_cat = 'I can write "I am" or "I\'m"'
double_quote_cat = """I don't like to use double quotes on
my sentences, it makes them \"cocky\". """
bell_cat = """I don't know what '\\a' do. \aPlease tell me.
 I already know it! It's a cat that makes sound!!!"""
backspace_cat = '\b'
formfeed_cat = "What does '\\f'? Let's \f try!"
linefeed_cat = "The '\\n' is the same as a new line. Look\nanother line!"
unicode_cat = "'\\N{Name}' Character named in the Unicode database. Let's try '\\N{cat}': \N{cat}"
carriage_cat = "Let's try the '\\r': Something\rSomeone."
bit_16_cat = "'\\u1234' = \u1234"
bit_32_cat = "'\\U0010ffff' = \U0010ffff"
vertical_tab_cat = "What '\\v' is used for? I can \v see it now."
octal_value_cat = "\110\145\154\154\157\40\127\157\162\154\144\41"
hex_value_cat = "\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21"

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(single_quote_cat)
print(double_quote_cat.replace('\n', ''))
print(bell_cat.replace('\n', ''))
print("If I'm wrote a mistakee\b on word 'mistake', I can"
" use the '\\b' ascii backspace to correct my error.")
print(formfeed_cat)
print(linefeed_cat)
print(unicode_cat)
print(carriage_cat)
print(bit_16_cat)
print(bit_32_cat)
print(vertical_tab_cat)
print(octal_value_cat)
print(hex_value_cat)
