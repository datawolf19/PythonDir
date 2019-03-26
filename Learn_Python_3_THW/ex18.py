def print_list(*args):
    text = ''
    for i, arg in enumerate(args, 1):
        text += f"arg{i}: {arg}, "
    print(text)


def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument

def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments

def print_none():
    print("I got nothing'.")

print_list("My", "name", "is", "Wolfgang", "Morton", "pleasure", "to", "meet", "you")
print_two("Wolfgang", "Morton")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()