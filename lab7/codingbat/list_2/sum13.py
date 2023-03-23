def sum13(nums):
  if len(nums)==0:
    return 0
    
  sum = 0
  
  if nums[len(nums)-1]==13:
    nums[len(nums)-1]=0
    
  for i in range(len(nums)-1):
    if nums[i]==13:
      nums[i]=0
      nums[i+1]=0

  for i in range(len(nums)):
    sum+=nums[i]
    
  return sum