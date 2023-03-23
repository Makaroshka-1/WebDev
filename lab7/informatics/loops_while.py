

def A(num):
    i=1
    while i<=num:
        print(i)
        i=i*2
def B(num):
    i=2
    while i<=num:
        if num%i==0:
            print(i)
            break
        i+=1
def C(num):
    i = 1
    while i<=num:
        print(i,end= ' ')
        i*=2         
def D (num): 
    i = 1
    while i<num:
        i*=2
    if i == num:
        print("YES")
    else:
        print("NO")
def E(num):
    i = 1 
    cnt = 0 
    while i<num:
        i=i*2
        cnt += 1
    print(cnt)