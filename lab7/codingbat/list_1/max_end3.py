def max_end3(nums):
  n = max(nums[0],nums[2])
  for i in range(len(nums)):
    nums[i]=n
  return nums