a = [4,2,0,1,0,3,0]

def beg_part(a):
  low_boundary = 0
  length = len(a)
  i = 0
  for i in range(0,length):
    if a[i] == 0:
      a[i],a[low_boundary] = a[low_boundary],a[i]
      low_boundary+=1
  return a
print(beg_part(a))

a = [4,2,0,1,0,3,0]

def end_part(a):
  high_boundary = len(a)-1

  i = 0
  for i in range(len(a)-1,0,-1):
    if a[i] == 0:
      a[i],a[high_boundary] = a[high_boundary],a[i]
      high_boundary-=1
  return a
print(end_part(a)) 
