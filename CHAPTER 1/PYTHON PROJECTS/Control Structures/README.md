#CONTROL STRUCTURES
Control structures or control statement are statements or block of code in a programming language that allow the programmer direct the order or flow of execution of a program,they are also used to specify the logical aspect of the program

##TYPES OF CONTROL STRUCTURES
- Conditional Statements
- Loops
- Functions


###CONDITIONAL STATEMENTS
Conditional statements are statements that define the logical aspect of the program, they allow certain parts of the code to run or produce certain result based on the condition placed in the program. Note that the result of conditional statements are boolean(True or False) we can do this by using 'if' statement, 'elif'(short for else if) statement and 'else' statement

- python code
gender = 'male'
if gender == 'male':
    print('Sir')
else:
    print('Ma')

The above code compares the value of the variable gender using the comparison operator(==) width the string ('male') if True print sir meaning if the value of the variable matches that of the string print 'sir' else print 'ma' 

A ROCK PAPER SCISSORS game has been created for you with **PYTHON** to fully understand the concept of conditional statement. See conditional.py


### Loops
Iteration also known as loops, this is a type of control structure that allows us as programmers to perform a particular task over a specified number of time, or the specified condition is met. Note there is a concept know as infinite loop,these are loops whose condition cannot be met or no condition was given hence the name **infinite** loop. Note just as indexing in python starts from 0  looping in python also starts from 0. For better understanding see iteration.py

In python when trying to loop we can either use the for loop or the while loop. When trying to loop a program for a specific number of times, it is better to use the for loop. But if it's for an infinite number of time use while loop.

###### FOR LOOP
For Loop is a control statement that allows a programmer to interate over a sequence of item, such as a list or an array and perform specific operation on individual elements in the sequence


