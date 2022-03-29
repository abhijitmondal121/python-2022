# l=eval(input("enter thew value of the list :"))
# l.sort()
# print(l[-2])



# l=eval(input("enter thew value of the list :"))
# nl=[]
# for i in l:
#     if i not in nl:
#         nl.append(i)
#     else:
#         print(i)    


# l=eval(input("enter thew value of the list :"))
# c=0
# sum=0
# for i in l:
#     sum+=i
#     c=c+1
# a=sum//c

# print("sum : ",sum)
# print("Avg : ",a)



# l=eval(input("enter thew value of the list :"))
# a=int(input("Enter the value : "))

# for i in l:
#     if i==a:
#         l.remove(i)
# print(l)        




# l=eval(input("enter thew value of the list :"))
# a=int(input("Enter the value : "))

# for i in l:
#     if i==a:
#         b=int(input("Enter the value you want to replace: "))
#         l[i]=b
#         # l.remove(i)
        
# print(l) 



# a=int(input("Enter the value : "))
# temp=a
# sum=0
# c=0
# while temp!=0:
#     temp//=10
#     c=c+1
# temp=a

# while a > 0:
#     r=a%10
#     f=pow(r,c)
#     sum=sum+f
#     a=a//10

# if temp==sum:
#     print("Armstrong Number :") 
# else:
#     print("Not Armstrong Number :") 


# a=int(input("Enter the value : "))
# temp=a
# rev=0
# while a > 0:
#     r=a%10
#     rev=rev*10+r
#     a//=10
# if temp==rev:
#     print("palindrome")
# else:
#     print(" Not palindrome")



a=int(input("Enter the value : "))
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i

if sum==a:
    print("perfect")
else:
    print("Not perfect")        
