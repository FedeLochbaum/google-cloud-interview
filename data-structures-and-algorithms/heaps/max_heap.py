from min_heap import *

class MaxHeap(MinHeap):
  
  def peek(self): return super().peek() * - 1

  def add(self, val): super().add(val * - 1)

  def pop(self): return super().pop() * - 1