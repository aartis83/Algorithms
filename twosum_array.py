a = [1,2,4,5,6]
target = 6

def twosum_array(a):

  start = 0
  end = len(a)-1
  while a[start]<a[end]:
    sum = a[start]+a[end]
    if sum < target:
      start+=1
    elif sum > target:
      end-=1
    else:
      return(start,end)
  return []
print(twosum_array(a))  
