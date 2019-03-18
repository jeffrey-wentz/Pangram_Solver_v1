import main_functions


while True:
    s_input = main_functions.get_input()
    is_pan = main_functions.is_pangram(s_input)

    if is_pan:
        print("Congratulations! " + s_input + " is a pangram!")
    else:
        print(s_input + " is not a pangram.")

    cont = input("Would you like to continue?: ")
    if cont.lower() in ("no", "n", 0):
        break
