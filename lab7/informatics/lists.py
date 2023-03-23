

def A(n):
    nums = [ ]
    for i in range(n):
        x = int(input())
        nums.append(x)
    for i in range(n):
        if i %2 == 0: 
            print(nums[i])

def B(n):
    nums = [ ]
    for i in range(n):
        x = int(input())
        nums.append(x)
    for i in range(n):
        if nums[i] % 2 == 0: 
            print(nums[i])

def C(n):
    nums = [ ]
    count = 0
    for i in range(n):
        x = int(input())
        nums.append(x)
    for i in range(n):
        if nums[i] > 0: 
            count +=1
    print(count)

def D(n):
    nums = [ ]
    count = 0
    for i in range(n):
        nums.append(int(input()))
    for i in range(n-1):
        if nums[i+1]>nums[i]:
            count +=1
    print(count)

def E(n):

    nums = [ ]
    flag = False
    for i in range(n):
        nums.append(int(input()))
    for i in range(n-1):
        if (nums[i+1]<0 and nums[i]<0) or (nums[i+1]>0 and nums[i]>0):
            flag = True
    if flag:
        print("yes")
    else:
        print("no")

def F(n):
    nums  = []
    count = 0 
    for i in range(n):
        nums.append(int(input()))
    for i in range(1,n-1):
        if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
            count +=1
    print(count)

def G(n):
    nums = [ ]
    for _ in range(n):
        nums.append(int(input()))
    for i in range(0,n//2):
        nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
    print(nums)