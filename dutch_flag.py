a = [3,2,1,4,5,8,10,12,7,4,6,4]
pivot = 6

def dutch_flag(a,pivot):
  low_boundary  = 0
  high_boundary = len(a)-1
  i = 0
  while i <= high_boundary:
    if a[i] < pivot:
      a[i],a[low_boundary] = a[low_boundary],a[i]
      low_boundary+=1
      i+=1
    elif a[i] > pivot:
      a[i],a[high_boundary] = a[high_boundary],a[i]
      high_boundary-=1
    else:
      i+=1
  return(a)

print(dutch_flag(a,pivot))
