"""
We were given 5 positive integers.
Now, we need to find the Minimum and Maximum values that can be gotten by
summing exactly four of the five integers.
"""
# Now, lets understand how this works; 
# Say we have three numbers 1,2,3; and we need to do the samething that we wrote up there (summing exactly two numbers this time)
# First thing, we get all the possible COMBINATIONS (1,2), (1,3), (2,3)
# Max = 5 and Min = 3

# We really do not want to go through the stress of getting all these possible combinations by ourselves
# As it may take ages, if we're dealing with large amount of numbers.


# This is why we have the itertools Module
# Itertool is a Module that is used to create iterations.
# It's efficient as its very fast and accurate.

# So, we import combinations from the Module, as thats what we'll work with. 
# The combinations helps us get the possible combinations that we need.
from itertools import combinations as cb

# This function will retrurn the Minimum and Maximum values...
# arr is the array of numbers...
def find_min_max(arr):

    # The next line helps us get all possible combinations
    # cb is the combination object; arr is the array and 4 is the number of integers that we want to  be grouped
    get_combinations = cb(arr, 4)

    # This is where we'll store all the sums of the possible combinations we got.
    new_arr = []

    # get_combinations really returns us an object; so we need to Loop through to get the values in it.
    for i in get_combinations:
        # we just want to get the sums of our various combinations and put them in this array.
        new_arr.append(sum(i))
    
    # min and max functions returns the minimum and maximum values in a List.
    minimum = min(new_arr)
    maximum = max(new_arr)

    # then, we return the values we needed; minimum and maxiuum values.
    return f"Max: {maximum}\nMin: {minimum}"

# Here, we invoke our function with the array in it.
print(find_min_max([1,2,3,4,5]))

