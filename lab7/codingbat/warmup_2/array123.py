def array123(nums):
  num = [1,2,3]
  for i in range(len(nums)-2):
    if num == nums[i:3+i]:
      return True
  return False
    
