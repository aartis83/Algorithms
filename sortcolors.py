nums = [2,0,2,1,1,0]

def sort_colors(nums):
  class Color(enumerate):
    red = 0
    white = 1
    blue = 2
  low_boundary = 0
  high_boundary = len(nums)-1
  i = 0
  while i <= high_boundary:
    color = nums[i]
    if color == Color.red:
      nums[i],nums[low_boundary] = nums[low_boundary],nums[i]
      low_boundary+=1
      i+=1
    elif color == Color.blue:
      nums[i],nums[high_boundary] = nums[high_boundary],nums[i]
      high_boundary-=1
    elif color == Color.white:
      i+=1
  return(nums)

print(sort_colors(nums))  
