
#
# def validator(valid_list, input_text):
#     input_text = input("Would you like to add a hero?")
#     if input_text =
#

def validator (list_of_valid_entries, input_text):
    is_valid = False
    while True:
        try:
            entry = input(input_text)
            for item in list_of_valid_entries:
                if item == entry:
                    is_valid = True
                else:
                    pass
            if is_valid:
                return entry
            else:
                print("Invalid Input! Try again...")
        except:
            print("Invalid Input! Try again...")

validator(["Yes","yes","y", "No", "no", "n"], "Would you like to add a hero? ")
