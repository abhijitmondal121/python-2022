def check(a):
    if a==0:
        return 0
    if a==1:
        return 1
    return check(a-1)+check(a-2);          

def lcm(a,b):
    h=a
    t=b
    while h!=t :
        if h>t:
            h-=t
        else:
            t-=h 
    lcm=(a*b)/h
    print("Lcm:",lcm)




print("Enter the number")
a=int(input())
# check(a)
print(check(a))
lcm(12,18)

