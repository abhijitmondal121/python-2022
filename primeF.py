from matplotlib.pyplot import flag


def check(a):
    flag=0
    for i in range (2,a):
        if a%i==0 :
            print("Not prime")
            flag=1
            break
    if flag==0:
        print("prime")


print("Enter the number")
a=int(input())

print(check(a))



