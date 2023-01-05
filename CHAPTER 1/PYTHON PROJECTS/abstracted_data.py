"""This code is the master code for all CSC 132 terminologies"""

# Introduction to data abstraction


"""Data abstraction or encapsulation is a programming language principle of hiding data 
using functions, libraries and modules, this gives room for flexibility of programmers
and writing readable and clean codes."""


def get_range(user_list):
    """This function is used to get the range of a particular set of data (numbers)."""

    def get_max_num(user_list):
        """This function is used to get the highest number in a given set of data"""
        max_val = 0
        for number in user_list:
            if number > max_val:
                max_val = number
            else:
                max_val = max_val

        return max_val

    def get_min_num(user_list):
        """This function is used to get the lowest number in a given set of data"""
        min_val = get_max_num(user_list)
        for value in user_list:
            if value < min_val:
                min_val = value
            else:
                min_val = min_val

        return min_val

    d_range = get_max_num(user_list) - get_min_num(user_list)

    return f'The range of the values {user_list} is {d_range}'


