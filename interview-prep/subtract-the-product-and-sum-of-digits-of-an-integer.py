from functools import reduce

# Given an integer number n,
# return the difference between the product of its digits and the sum of its digits.

def get_digits(number):
  digits = []
  while number > 0:
    digits.append(number % 10)
    number //= 10

  digits.reverse()
  return digits

mul = lambda n: reduce(lambda a, b: a * b, n)

def subtract_product_and_sum(n):
  dig = get_digits(n)
  return mul(dig) - sum(dig)

def subtract_product_and_sum(n):
  dig = get_digits(n)
  return abs(sum(dig) - mul(dig))
