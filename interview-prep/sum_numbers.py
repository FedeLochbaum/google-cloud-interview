
# Given a string, return the sum of the numbers appearing in the string,
# ignoring all other characters. A number is a series of 1 or more digit chars in a row.
# (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'.
# Integer.parseInt(string) converts a string to an int.)

# sum_numbers("abc123xyz") → 123
# sum_numbers("aa11b33") → 44
# sum_numbers("7 11") → 18

def is_int(str):
  try: int(str); return True
  except: return False

def get_str_num(_str, _from):
  _to = _from + 1
  while(_to < len(_str) and is_int(_str[_to])): _to += 1
      
  return _str[_from:_to:]

def sum_numbers(_str):
  pointer = 0
  sum = 0
  while(pointer < len(_str)):
    n = 1
    if is_int(_str[pointer]):
      sub_str = get_str_num(_str, pointer)
      sum += int(sub_str)
      n = len(sub_str)
    pointer += n

  return sum

print(sum_numbers('abc123xyz'))
print(sum_numbers('aa11b33'))
print(sum_numbers('7 11'))