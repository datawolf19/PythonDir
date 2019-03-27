from sys import argv

script, input_file = argv

# Defining the functions for this script.

# This function reads the file and prints its contents.
def print_all(f):
    print(f.read())

# Goes to the start of the file.
def rewind(f):
    f.seek(0)

# Prints out the line number and a single line is read
# and printed to the user.
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

for x in range(1, 4):
    print_a_line(x, current_file)
    
