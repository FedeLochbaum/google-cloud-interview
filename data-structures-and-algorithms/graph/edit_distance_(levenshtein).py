def edit_distance(str1, str2):
  len_s1, len_s2 = len(str1), len(str2)

  dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
  # matrix dp represents the distance between the first i chars of the first string and the first j chars of the second string

  for i in range(len_s1 + 1): dp[i][0] = i
  for j in range(len_s2 + 1): dp[0][j] = j

  for i in range(1, len_s1 + 1):
    for j in range(1, len_s2 + 1):
      cost = 0 if str1[i-1] == str2[j-1] else 1
      # the caracter (i - 1) of the string1 is different of character (j - 1) of the string2
      dp[i][j] = min(
        dp[i - 1][j] + 1,  # Eliminación
        dp[i][j - 1] + 1,  # Inserción
        dp[i - 1][j - 1] + cost  # Sustitución
      )

  return dp[len_s1][len_s2]

s1 = "kitten"
s2 = "sitting"
print(edit_distance(s1, s2)) # 3