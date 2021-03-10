s = 'go back'

def reverseword(s):
  if s =="":
    return("")

  result = ""
  i = len(s)-1
  end = len(s)
  while i>=0:
    if s[i]!=" ":
      i-=1
    else:
      result+=s[i+1:end+1] + " "
      i-=1
      end = i
  result+=s[i+1:end+1]
  return(result)

print(reverseword(s))
