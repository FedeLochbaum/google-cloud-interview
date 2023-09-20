# Have the function first_reverse(str) take the str parameter being passed and return the string in reversed order.
# For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

# Examples
# Input: "coderbyte"
# Output: etybredoc

# Input: "I Love Code"
# Output: edoC evoL I

def first_reverse(_str): return ''.join(reversed(_str))

print(first_reverse('coderbyte') == 'etybredoc')
print(first_reverse('I Love Code') == 'edoC evoL I')