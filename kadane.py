
a = [-1,-23,-8,0,-6]
def kadane(a):
  cur_start = 0
  cur_end = 0
  start = 0
  end = 0
  cur_sum = a[0]
  max_sum = a[0]
  for i in range (1,len(a)):
    if cur_sum + a[i] > a[i]:
      cur_end = i
      cur_sum+=a[i]
    else:
      cur_start = i
      cur_end = i
      cur_sum = a[i]
    if (max_sum < cur_sum):
      max_sum = cur_sum
      start = cur_start
      end = cur_end
  print ("Start :"+ str(start))
  print("End :" + str(end))
  print ("Maxsum :" + str(max_sum))
  return max_sum
print (kadane (a))

# Just the max_sum using kadane

a = [-1,-23,-8,-6]
def kadane(a):
  cur_sum = a[0]
  max_sum = a[0]
  for i in range (1,len(a)):
    cur_sum = max(cur_sum + a[i], a[i])
    max_sum = max(max_sum ,cur_sum)
  print ("Maxsum :" + str(max_sum))
  return max_sum
print (kadane (a))
