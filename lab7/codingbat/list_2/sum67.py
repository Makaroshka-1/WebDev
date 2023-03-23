def sum67(nums):
    flag=False
    sum=0
    for i in range(len(nums)):
        if flag == False:
            if nums[i] == 6:
                flag=True
            else:
                sum+=nums[i]
        else:
            if nums[i] == 7:
                flag=False
    return sum