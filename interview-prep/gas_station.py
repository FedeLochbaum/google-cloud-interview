# Given two integer arrays A and B of size N. There are N gas stations along a circular route, where the amount of gas at station i is A[i].

# You have a car with an unlimited gas tank and it costs B[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

# Return the minimum starting gas station's index if you can travel around the circuit once, otherwise return -1.

# You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2.. Completing the circuit means starting at i and ending up at i again.

# Problem Constraints
# 1 <= |A| <= 5 * 105
# |A| == |B|
# 0 <= Ai <= 5 * 103
# 0 <= Bi <= 5 * 103

# Input Format
# The first argument given is the integer array A. The second argument given is the integer array B.

# Output Format
# Return the minimum starting gas station's index if you can travel around the circuit once, otherwise return -1.=

# Example Input
# A = [1, 2]
# B = [2, 1]


# Example Output
# 1

# Example Explanation
# If you start from index 0, you can fill in A[0] = 1 amount of gas.
# Now your tank has 1 unit of gas. But you need B[0] = 2 gas to travel to station 1.

# If you start from index 1, you can fill in A[1] = 2 amount of gas.
# Now your tank has 2 units of gas. You need B[1] = 1 gas to get to station 0.
# So, you travel to station 0 and still have 1 unit of gas left over.
# You fill in A[0] = 1 unit of additional gas, making your current gas = 2. It costs you B[0] = 2 to get to station 1, which you do and complete the circuit.

def can_complete_circuit(A, B):
  # cost from station i to i + 1 = B[i]
  # gas in station i = A[i]

  # return the minimum starting station point index in order to travel around the circuit once

  # shortest_path the cost of i to i + 1 is Prev + A[i] - B[i], You can only travel in one direction
  total_gas = 0
  current_gas = 0
  start_station = 0

  for i in range(len(A)): # for each station base amount
    i = i % len(A)
    diff = A[i] - B[i] # this is the cost to go to i + 1
    current_gas += diff
    total_gas += diff

    if current_gas < 0: # if the current gas is negative, then it wasn't enough to travel
      current_gas = 0 # restart
      start_station = i + 1

  return start_station if total_gas >= 0 else - 1

print(can_complete_circuit([1, 2], [1, 2]))