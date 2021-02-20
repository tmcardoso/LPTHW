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

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(single_quote_cat)
print(double_quote_cat.replace('\n', ''))
print(bell_cat.replace('\n', ''))
print("If I'm wrote a mistakee\b on word 'mistake', I can"
" use the '\\b' ascii backspace to correct my error.")
