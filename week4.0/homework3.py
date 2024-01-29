# get two numeric values from user
print("Enter me two numbers, Please")
print("#1")
first_number = int(input("> "))
print()

print("#2")
second_number = int(input("> "))
print()

addition = first_number + second_number
print("{} + {} = {}".format(first_number, second_number, addition))

subtraction = first_number - second_number
print("{} - {} = {}".format(first_number, second_number, subtraction))

division = first_number / second_number
print("{} / {} = {}".format(first_number, second_number, division))

multiplication = first_number * second_number
print("{} * {} = {}".format(first_number, second_number, multiplication))

mod = first_number % second_number
print("{} % {} = {}".format(first_number, second_number, mod))

not_remaining_number = first_number // second_number
print("{} // {} = {}".format(first_number, second_number, not_remaining_number))
