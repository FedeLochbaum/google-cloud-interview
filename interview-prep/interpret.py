
# Write a simple interpreter which understands "+", "-", and "*" operations.
# Apply the operations in order using command/arg pairs starting with the initial value of `value`.
# If you encounter an unknown command, return -1.
# interpret(1, ["+"], [1]) → 2 interpret(4, ["-"], [2]) → 2 interpret(1, ["+", "*"], [1, 3]) → 6

# interpret(1, ['+'], [1]) → 2
# interpret(4, ['-'], [2]) → 2
# interpret(1, ['+', '*'], [1, 3]) → 6

OPS = {
  '+': lambda x, y: x + y,
  '-': lambda x, y: x - y,
  '*': lambda x, y: x * y
}

def interpret(base, commands, args):
  curr = base
  for cmd in commands:
    if cmd not in OPS: return -1
    curr = OPS[cmd](curr, args.pop(0))
  
  return curr

print(interpret(1, ['+'], [1]))
print(interpret(4, ['-'], [2]))
print(interpret(1, ['+', '*'], [1, 3]))