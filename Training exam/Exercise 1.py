# Given integers n and k, return a list 
# of length n containing 0 1 2 ... k-1 0 1 2 ... k-1 ...
# n times. 

def repeatSequence(n, k):
  lst = []
  
  for time in range(n):
     lst += [number for number in range(k)]
  
  return lst
