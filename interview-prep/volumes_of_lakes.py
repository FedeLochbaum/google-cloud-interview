# The Challenge
# Imagine an island that is in the shape of a bar graph.
# When it rains, certain areas of the island fill up with rainwater to form lakes.
# Any excess rainwater the island cannot hold in lakes will run off the island to the west or east and drain into the ocean.

# Given an array of positive integers representing 2-D bar heights, design an algorithm (or write a function) that can compute the total volume (capacity) of water that could be held in all lakes on such an island given an array of the heights of the bars. Assume an elevation map where the width of each bar is 1.

# Example: Given [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2], return 15 (3 bodies of water with volumes of 1,7,7 yields total volume of 15)

# An image showing the volume of water
# Learning objectives
# This question offers practice with algorithms, data structures, Big-O, defining functions, generalization, efficiency, time and space complexity, and anticipating edge cases.

def trap(heights):
  left_max = [0] * len(heights)
  right_max = [0] * len(heights)

  left_max[0] = heights[0] # Keep an arrray comparing with the left limit
  for i in range(1, len(heights)): left_max[i] = max(left_max[i - 1], heights[i])

  right_max[-1] = heights[-1] # Keep an arrray comparing with the right limit
  for i in range(len(heights) - 2, -1, -1): right_max[i] = max(right_max[i + 1], heights[i])

  total_water = 0
  for i in range(len(heights)):
    total_water += min(left_max[i], right_max[i]) - heights[i]

  return total_water

print(trap([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]))