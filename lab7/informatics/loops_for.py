import math
def A(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i,end =' ')
            
def B(a,b,c,d):
    for i in range (a,b+1):
        if i%d==c:
            print(i, end = ' ')

def C(a,b):
    for i in range(a,b+1):
        if (math.sqrt(i) ** 2) == i:
            print(i,end= ' ')

def D(x,d):
    x = str(x)
    count = 0
    for i in range(len(x)):
        if int(x[i])==d:
            count +=1
    print(count)

def E(num):
    num = str(num)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    print(sum)

def F(num):
    num=str(num)
    print(int(num[::-1]))

def G(num):
    for i in range(2,num+1):
        if num%i==0:
            print(i)
            break

def H(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=' ')

def I(num):
    sum=0
    for i in range(1,num+1):
        if num%i==0:
            sum+=1          
    print(sum)

def J():
    sum=0
    for i in range(100):
        x = int(input())
        sum += x
    print(sum)

def K(n):
    sum = 0 
    for i in range(n):
        x = int(input())
        sum+=x
    print(x)

def L(num):
    sum = 0
    n=len(num)
    for i in range(n-1,-1,-1):
        if int(num[n-1-i])==1:
            sum +=2**i     
    print(sum)


def M(n):
    count = 0
    for i in range(n):
        x = int(input())
        if x == 0:
            count+=1
    print(count)
 
