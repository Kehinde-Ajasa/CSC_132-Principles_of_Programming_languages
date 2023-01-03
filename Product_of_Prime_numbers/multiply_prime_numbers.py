"""This program helps in multiplying an amount of prime numbers
program must first check if number entered by user are prime or not"""

from Primenumbers import is_prime_number


def user_input():
    """Accepting all user's input and performing operation"""
    product = 1
    prime_number_list = list()
    amount_of_numbers = int(input("How many prime numbers do you want to multiply: "))
    for i in range(1, amount_of_numbers + 1):
        p_number = int(input(f"Enter your {i} number: "))
        while (is_prime_number(p_number)) != 1:
            print("The number you entered is not a prime number, Try again")
            p_number = int(input(f"Enter your {i} number: "))
        if is_prime_number(p_number) == 1:
            prime_number_list.append(p_number)
            product *= p_number

    return f'The Product of the prime numbers {prime_number_list} is {product}'


"""def multiply_numbers(num):
    product = 1
    for k in num:
        product *= k

    return product"""


print(user_input())
