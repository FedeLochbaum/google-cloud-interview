# Fix this duplicate collapsing code:
# public String collapseDuplicates(String a) {
#   int i = 0;
#   String result = "";
#   while (i < a.length()) {
#     char ch = a.charAt(i);
#     result += ch;
#     while (a.charAt(i+1) == ch) { i++; } i++;
#   }
#   return result;
# }

# collapse_duplicates("a") → "a"
# collapse_duplicates("aa") → "a"
# collapse_duplicates("abc") → "abc"

def collapse_duplicates(_str):
  res = ''
  for i in range(len(_str)):
    ch = _str[i]
    if i == 0 or ch != _str[i - 1]: res += ch
  
  return res

print(collapse_duplicates("a"))
print(collapse_duplicates("aa"))
print(collapse_duplicates("abc"))