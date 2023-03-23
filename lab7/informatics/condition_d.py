def sign(num):
    if num==0:
        return 0
    elif num>0:
        return 1
    else:
        return -1
x = int(input())
print(sign(x))