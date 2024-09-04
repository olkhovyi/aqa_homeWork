# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

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
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def calculating_function(num1, num2, operation="+"):
    result = None
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "*":
        result = num1 * num2
    return result

print(f"2. Calculating result: {(calculating_function(5, 2, operation="-"))}")
print("-" * 100)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(numbers):

    # Will calculate the arithmetic mean of a list of numbers
    result = sum(numbers) / len(numbers)
    return result

print(f"3. Average: {(arithmetic_mean([3, 2, 10, 20, 30]))}")
print("-" * 100)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(some_string):

    # return string in reverse order
    result = some_string[::-1]
    return result

print(f"4. Reverse string result: {(reverse_string("My name is Alex"))}")
print("-" * 100)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
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
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    index = str1.find((str2))
    return index

str1 = "Hello, world!"
str2 = "world"
print(f"6. Find substring: {(find_substring(str1, str2))}") # поверне 7
''
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
the string variables that are present in lst1. The data in the letter can be any"""

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
"""There is a sheet with numbers, calculate the sum of all EVEN numbers in this sheet"""
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
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""