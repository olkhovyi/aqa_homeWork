string_list = ["1,3,5,7", "2,4,6,8", "9,w,r,10"]

def sum_function(s):
    try:
        # break the string with a comma
        numbers = s.split(",")
        total = 0
        # iterate over each element string
        for num in numbers:
            total += int(num)

        return total
    except ValueError:
        # if there are non-numeric characters in the line, we display a message
        return "I can't do it"

# iterate over each element list
for s in string_list:
    result = sum_function(s)
    print(result)