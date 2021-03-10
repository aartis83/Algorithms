nums = [0,7,8,3,2,3]
target = 9

def two_sum(nums,target):
  value = dict()
  for i,num in enumerate(nums):
    compl = target - num
    if compl in value:
      return(value[compl],i)
    value[num] = i
  return []
print(two_sum(nums,target))
