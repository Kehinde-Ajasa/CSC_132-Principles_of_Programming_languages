"""This program helps in multiplying an amount of prime numbers
program must first check if number entered by user are prime or not"""

from Primenumbers import is_prime_number


ord_dict = {1:'1st', 2:'2nd', 3:'3rd'}

def user_input():
    """Accepting all user's input and performing operation"""
    product = 1

    #Changing the list initialization from list() to open-close square brackets as this is more effective more pythonic
    prime_number_list = []
    amount_of_numbers = int(input("How many prime numbers do you want to multiply: "))

    for i in range(1, amount_of_numbers + 1):
        #Allowing for capabilities to handle any arbitrary values passed by the user
        p_number = int(input(f"Enter your {(ord_dict[i] if i in ord_dict.keys() else (str(i)+'th'))} number: "))

        while (is_prime_number(p_number)) != 1:
            print("The number you entered is not a prime number, Try again")
            p_number = int(input(f"Enter your {i} number: "))
        if is_prime_number(p_number) == 1:
            prime_number_list.append(p_number)
            product *= p_number

    #Changing our `return` statement to return the `product value` while printing out the report string to the user
    #This will allow the function to be useable in any other module.
    print(f"The Product of the prime numbers {','.join(str(num) for num in prime_number_list[:-1])} and {prime_number_list[-1]} is {product}")
    return product


user_input()