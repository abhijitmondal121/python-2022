# n=0
# while n<10:
#     print(n,end=" ")
#     n=n+1

# do{
#     n=0
#     print(n,end=" ")
#     n=n+1

# }
# while n<10;


# n=int(input("Enter the number of term"))
# v=int(input("Enter the value"))

# sum=0
# p=0
# d=0
# for i in range(1,n+1):
#     p=pow(v,i)
#     d=p/i
#     sum=sum+d
# print(sum)

n=int(input("Enter the number of term"))
n1=0
n2=1
print (n1)
print (n2)

for i in range(2,n):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3

