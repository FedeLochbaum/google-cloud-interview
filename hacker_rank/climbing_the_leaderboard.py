# An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

# The player with the highest score is ranked number  on the leaderboard.
# Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

# Example

# The ranked players will have ranks , , , and , respectively. If the player's scores are ,  and , their rankings after each game are ,  and . Return .

# Function Description

# Complete the climbingLeaderboard function in the editor below.

# climbingLeaderboard has the following parameter(s):

# int ranked[n]: the leaderboard scores
# int player[m]: the player's scores
# Returns

# int[m]: the player's rank after each new score
# Input Format

# The first line contains an integer , the number of players on the leaderboard.
# The next line contains  space-separated integers , the leaderboard scores in decreasing order.
# The next line contains an integer, , the number games the player plays.
# The last line contains  space-separated integers , the game scores.

# Constraints

#  for 
#  for 
# The existing leaderboard, , is in descending order.
# The player's scores, , are in ascending order.
# Subtask

# For  of the maximum score:

def get_pos_with_binary_search(play, rank):
  if play >= rank[0]: return 1
  if play <= rank[-1]: return len(rank) + 1
  
  left, right = 0, len(rank) - 1
  while(left <= right):
    mid = (left + right) // 2
    if rank[mid] == play: return mid + 1

    if rank[mid] > play: left = mid + 1
    else: right = mid - 1
    
  return left + 1

def climbing_leaderboard(ranked, player):
  rank = sorted(set(ranked), reverse = True) # [100, 50, 40, 40, 20, 10]
  return list(map(lambda play: get_pos_with_binary_search(play, rank), player))

print(climbing_leaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])) #[6, 4, 2, 1]
print(climbing_leaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])) #[6, 5, 4, 2, 1]