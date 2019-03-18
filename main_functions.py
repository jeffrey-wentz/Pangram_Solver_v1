

# gets the string from user and verifies it contains only letters or spaces
def get_input():
    # loops until desired input
    while True:
        user_string = input("Please enter your word: ")
        # all() returns true if each char in user_string is alpha or a space
        if all(x.isalpha() or x.isspace() for x in user_string):
            return user_string
        else:
            print("You must enter a string!")


# checks if the user's string is a pangram by creating an empty set and checks each char in s_input
# if the char is alpha then it gets added to the empty set
def is_pangram(s_input):
    pangram_list = set()

    for char in s_input:
        if char.isalpha():
            pangram_list.add(char.lower())

    # duplicate letters do not affect result as sets ignore
    return len(pangram_list) == 26


