a = [-4,-1,2,4,6]

def squares(a):
  if len(a) == 0:
    return []
  result = []
  start = 0
  end = len(a)-1
  while start<=end:
    if abs(a[start]) > abs(a[end]):
      result.append((a[start])**2)
      start+=1
    elif abs(a[start]) <= abs(a[end]):
      result.append(a[end]**2)
      end-=1
  return(result [::-1])
print(squares(a))

a = [-4,-2,-1,0,2,3,6]

# 1, 2, 3
# start 1 end 3
# start 2 end 2
def squares(a):
  if len(a) == 0:
    return []
  result = []
  rend = len(result)-1
  start = 0
  end = len(a)-1

  while start<=end:
    if abs(a[start]) > abs(a[end]):
      result.insert(rend,(a[start])**2)
      start+=1
    else:
      result.insert(rend,a[end]**2)
      end-=1
    rend-=1
  return(result)
print(squares(a))
