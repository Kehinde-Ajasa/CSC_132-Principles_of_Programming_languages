"""
Factorial in mathematics is the result of multiplying
consecutive INTEGERS from 1 to the given character_change.
It's denoted with '!'
as in; n! = 1 * 2 * 3 * (n-1) * n
"""

# First, we create a Function; called Factorial
# This is the function that computes the value of the factorial
# We've also set a parameter 'num' there; 
# num represents the factorial of the character_change we're looking for.

def factorial(num):
    # Then, we initialized a variable called fact and gave it a value of 1
    #  This is because we're computing the value of the factorial from 1*2*....
    # Giving it another value to begin with will return wrong answers
    fact = 1
    
    #  Using a for loop;
    # A loop is a block of code that runs till the condition is false, or till its broken
    for i in range(1, num +1):
        # In this for loop; the value of 'i' begins from 1; 
        # and it has an increment of 1 as the loop reruns till the condition of the loop is no more satisfied
        fact = fact * i
    
    # the return keyword converts this statement to something like a variable
    # so, anywhere this function is called, it returns this value (fact)
    return fact

#outside the function

# This next line gets the character_change whose factorial we're looking for : input()
# Then this value is converted to an integer int()
num = int(input("Find the factorial of > "))

# Finally we invoke the function
print(factorial(num))

"""
Writing your codes in simpler english before coding is a good Practice; this is called a Pseudo-code
You can also draw a Flow chart to represent your steps; this is called an algorithm

This will make your life much more easier.
"""
