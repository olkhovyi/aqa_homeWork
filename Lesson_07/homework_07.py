# task 1
""" The task is to print a multiplication table by a given number, but
only up to the maximum value for the product - 25.
The code is almost ready, it is necessary to find errors and correct/complement."""

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier

        # Stop the loop if the result exceeds 25
        if  result > 25:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

print("1. Table of multiplication by a given number: ")
(multiplication_table(3))
print("-" * 100)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Write a function that calculates the sum of two numbers."""

def calculating_function(num1, num2):

    return num1 + num2

print(f"2. Sum of two numbers: {(calculating_function(12, 2))}")
print("-" * 100)

# task 3
"""  Write a function that calculates the arithmetic mean of a list of numbers."""

def arithmetic_mean(numbers):

    # Will calculate the arithmetic mean of a list of numbers
    result = sum(numbers) / len(numbers)
    return result

print(f"3. Average: {(arithmetic_mean([3, 2, 10, 20, 30]))}")
print("-" * 100)

# task 4
"""  Write a function that takes a string and returns it in reverse order."""

def reverse_string(some_string):

    # return string in reverse order
    result = some_string[::-1]
    return result

print(f"4. Reverse string result: {(reverse_string("My name is Alex"))}")
print("-" * 100)

# task 5
"""  Write a function that takes a list of words and returns the longest word in the list."""
def find_longest_word(some_list):

    # Let's initialize a variable to store the longest word
    longest_word = some_list[0]

    for word in some_list:
        # If the current word is longer than the stored word, update the variable
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(f"5. Longest word result: {(find_longest_word(["Banana", "Road", "Congratulations"]))}")
print("-" * 100)

# task 6
"""  Write a function that accepts two strings and returns the index of the first occurrence of the second string
to the first row if the second row is a substring of the first row, and -1 if the second row
is not a substring of the first line. """

def find_substring(str1, str2):
    index = str1.find((str2))
    return index

str1 = "Hello, world!"
str2 = "world"
print(f"6. Find substring: {(find_substring(str1, str2))}") # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(f"   Find substring: {(find_substring(str1, str2))}") # поверне -1
print("-" * 100)

# task 7
"""Count the number of unique characters in a line. If there are more than 10 - display True in the console, 
otherwise - False."""

def unique_elements(some_string):

    # Use set to check whether all elements are unique
    unique_el = set(some_string)
    if len(unique_el) > 10:
        return True
    else:
        return False

print(f"7. Unique characters: {(unique_elements("My name is Alexandr"))}")
print("-" * 100)

# task 8
"""Write a function with a loop that will require the user to enter a word that contains the letter "h" 
(both uppercase and lowercase). The loop should not terminate if the user entered a word without the letter "h"."""

def word_with_specific_letter(word):
    while True:
        # Check whether the specified letter is in the word
        if 'h' in word or 'H' in word:
            break
        else:
            return "This word does not contain the letter 'h' or 'H'. Try again."

print(f"8. Word that contains the letter 'h' or 'H': {(word_with_specific_letter("Alex"))}")
print("-" * 100)

# task 9
"""There is a list with data lst1. Write a function that creates a new list (for example, lst2) that contains only 
the string variables that are present in lst1. The data in the letter can be any."""

def only_string(lst1):
    lst2 = []
    # Iterate over each element
    for i in lst1:
        # Element type check
        if isinstance(i, str):
            lst2.append(i)
    return lst2

print(f"9. That contains only the string variables: "
      f"{(only_string(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']))}")
print("-" * 100)

# task 10
"""There is a sheet with numbers, calculate the sum of all EVEN numbers in this sheet."""

def even_numbers(numbers):
    # Initialize a variable for storing even numbers
    even_sum = 0
    # Iterate over each element
    for num in numbers:
        # Find even numbers through division with a remainder
        if num % 2 == 0:
            even_sum += num
    return even_sum

print(f"10. The sum of all even numbers: {(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))}")
print("-" * 100)
