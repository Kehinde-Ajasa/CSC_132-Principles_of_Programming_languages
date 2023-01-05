"""This program helps in multiplying an amount of prime numbers
program must first check if number entered by user are prime or not"""

from Primenumbers import is_prime_number


ordinal_dictionary = {'1': 'st', '2': 'nd', '3': 'rd'}  # Dictionary to help understand the numbers displayed


def user_input():
    """Accepting all user's input and performing operation"""
    product = 1
    prime_number_list = []  # creating a list
    amount_of_numbers = int(input("How many prime numbers do you want to multiply: "))
    
    for i in range(1, amount_of_numbers + 1):
        # Allowing for capabilities to handle any arbitrary values passed by the user
        character_change = str(i)
        length_of_char = len(character_change)
        if length_of_char == 1:
            if character_change[-1] in ordinal_dictionary:
                p_number = int(input(f"Enter your {i}{ordinal_dictionary[character_change[-1]]} number: "))
            else:
                p_number = int(input(f"Enter your {i}th number: "))
        else:
            if character_change[-1] in ordinal_dictionary and character_change[-2] != "1":
                p_number = int(input(f"Enter your {i}{ordinal_dictionary[character_change[-1]]} number: "))
            else:
                p_number = int(input(f"Enter your {i}th number: "))

        while (is_prime_number(p_number)) != 1:
            print("The number you entered is not a prime number, Try again")
            p_number = int(input(f"Enter your {i} number: "))
        if is_prime_number(p_number) == 1:
            prime_number_list.append(p_number)
            product *= p_number

    print(f"The Product of the prime numbers {','.join(str(num) for num in prime_number_list[:-1])} and {prime_number_list[-1]} is {product}")
    return product


user_input()
