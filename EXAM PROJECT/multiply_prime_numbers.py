"""This program helps in multiplying an amount of prime numbers
program must first check if character_change entered by user are prime or not"""

from Primenumbers import is_prime_number


def ordination(number):
    """Helping to output the position of each numbers in an english like manner"""
    ordinal_dictionary = {'1': 'st', '2': 'nd', '3': 'rd'}    # Dictionary to help display numbers in ordinal form
    character_change = str(number)
    length_of_char = len(character_change)
    if length_of_char == 1:
        if character_change[-1] in ordinal_dictionary:
            p_number = character_change + ordinal_dictionary[character_change[-1]]
        else:
            p_number = character_change + "th"
    else:
        if character_change[-1] in ordinal_dictionary and character_change[-2] != "1":
            p_number = character_change + ordinal_dictionary[character_change[-1]]
        else:
            p_number = character_change + "th"
    return p_number


def user_input():
    product = 1
    prime_number_list = []  # creating a list
    amount_of_numbers = int(input("How many prime numbers do you want to multiply: "))
    
    for i in range(1, amount_of_numbers + 1):
        # Allowing for capabilities to handle any arbitrary values passed by the user
        a_number = int(input(f"Enter your {ordination(i)} number: "))

        while (is_prime_number(a_number)) != 1:
            print("The character_change you entered is not a prime number, Try again")
            a_number = int(input(f"Enter your {ordination(i)} number: "))
        if is_prime_number(a_number) == 1:
            prime_number_list.append(a_number)
            product *= a_number

    print(f"The Product of the prime numbers {','.join(str(num) for num in prime_number_list[:-1])} and {prime_number_list[-1]} is {product}")
    return product


user_input()
