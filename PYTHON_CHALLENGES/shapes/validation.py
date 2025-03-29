def validate_input_num(number):
    while True:
        try:
            number = int(number)
            if number > 0:
                return number
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid Input. Please enter a valid input.")
