import sys

n = None
book = {}

for line in sys.stdin:
  if n == None: n = int(line); continue
  if n > 0:
    name, num = line[:-1].split(' ')
    book[name] = int(num)
    n -= 1; continue
  name = line[:-1]
  if not name in book: print('Not found'); continue
  
  print(name + '=' + str(book[name]))