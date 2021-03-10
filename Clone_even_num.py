a = [0,7,6,3,8,-1,-1,-1]

def clone_even_num(a):
  end = len(a)
  i = last_num(a)
  if (a=='null'or a==0):
    return a
  while i>=0:
    if(a[i]%2 == 0):
      end = end-1
      a[end]=a[i]
    end = end-1
    a[end]=a[i]
    i-=1
  return a

def last_num(a):
  i=len(a)-1
  while(i>=0 and a[i]==-1):
    i-=1
  return i

print(clone_even_num(a))
