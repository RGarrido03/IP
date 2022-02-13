# Given a sequence lst, return the longest n so that 
# the first n elements equal the last n elements (with no overlapping).

# Dada uma sequência lst, devolva o maior n tal que
# os primeiros n elementos igualam os últimos n elementos (sem sobreposição).

def firstEqualLast(lst):
  mid = len(lst)//2
  n = 0
  for time in range(mid):
     if lst[0:time+1] == lst[len(lst)-time-1:]:
        n = time + 1
  
  return n
