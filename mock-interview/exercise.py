# There is a N player tournament. Players have rank 1 to N and each player has a unique rank. Assume that the best player always wins, where the best player is the player with rank 1.

# The tournament is a knockout tournament. This means if we have 8 players with their ranks [1 2 3 4 5 6 7 8], the tournament will look like this:
# 1st round: [1 2] [3 4] [5 6] [7 8]
# 2nd round: [1 3] [5 7]
# 3rd round: [1 5]
# champion : [1]

# We are calling [1 2 3 4 5 6 7 8] a "draw" where in the 1st round: the first two players meet in the first match, the next two players meet in the second match, and so on.

# In the 2nd round: in the first match, the winner of the first match of the 1st round and the winner of the second match of the 1st round will play together. And similarly, in the second match, the winner of the third match of the 1st round and the winner of the fourth match of the 1st round will play together.

# In short: given a draw, if we don't change the order of the players, players will meet in their order on the draw, and of course the winner moves to the next round. The tournament ends when there is only a single player remaining.

# A draw is a valid draw when in each round, the best (based on rank) player plays with the worst player, the second best player plays with the second worst player, and so on.

# Input: [1,8, 2, 7, 3, 6, 4, 5] Output: False
# [1 8] [2 7] [3 6] [4 5]
# [1 2] [3 4]

# [1 4 2 3] Output: True
# [1 2]
# [1]
# Problem 1:
# Given a draw, find out whether it is a valid draw.

# [3 2 1 4] Output: True

# [4 8, 5, 6, 2, 3 ]


# Round 1: Len = 8
# (1 8) (4 5) (3 6) (2 7) 

# Round 2: Len = 4
# [1 4 3 2]
# (1 4) (3 2)

# ROund 3: 
# (1 2)

# [1 8 2 7 3 6 4 5] = False

# (1 8) (2 7) (3 6) (4 5)

# [1 2 3 4] Len = 4
# (1 2)

def solve(tournament):
  while(len(tournament) > 1):
    _len = len(tournament) # len is the maximum
    winners = []
    for i in range(0, _len, 2):
      player1 = tournament[i]
      player2 = tournament[i + 1]
      if (player1 + player2 != _len + 1): return False
      winners.append(min(player1, player2))
    
    tournament = winners
  return True

print(solve([3, 2, 1, 4]) == True)
print(solve([1, 8, 2, 7, 3, 6, 4, 5]) == False)
print(solve([1, 8, 4, 5, 3, 6, 2, 7]) == True)