a = [1,3,5,2,6,4,7,8,9]

def FindUnsortedSubArray(a):

  n = len(a)
  cur_max = a[0]
  r = 0
  for i in range(1,n):
    if a[i] < cur_max:
      r = i
    else:
      cur_max = a[i]

  cur_min = a[-1]
  l =0
  for i in range(n-2,-1,-1):
    if a[i] > cur_min:
      l = i
    else:
      cur_min = a[i]

  return r-l+1 if l!=r else 0

print(FindUnsortedSubArray(a))  
