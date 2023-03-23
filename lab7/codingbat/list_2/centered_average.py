def centered_average(nums):
  x = nums.index(max(nums))
  y = nums.index(min(nums))
  nums[x]=0
  nums[y]=0
  sum = 0
  for i in range(len(nums)):
    sum += nums[i]
  if x==y:
    return sum//(len(nums)-1)
  return sum//(len(nums)-2)