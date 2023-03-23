def array_front9(nums):
    for i in range(len(nums)):
      if nums[i]==9:
        return True
      if i==3:
        return False
    return False