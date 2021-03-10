a = [6,5,4,3,2,1,0]

def reverse(a):
  if a is None:
    return []
  start = 0
  end = len(a)-1
  while a[start]>a[end]:
    a[start],a[end]=a[end],a[start]
    start+=1
    end-=1
  return a
print(reverse(a))
