# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    result = []
    for i in range (num, -1, -1):
        result.append(i)
    return result

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([2,5]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

print(first_plus_length([2,4,6,7]))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def greater_than_second(list):
    new_list = []
    if len(list)<2:
        return False
    for i in range (0, len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    return new_list
    

print(greater_than_second([7,3,8,1,9,6]))
print(greater_than_second([1]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(size, value):
    new_list = []
    for i in range (0, size):
        new_list.append(value)
    return new_list

print(length_and_value(3,5))
print(length_and_value(6,7))