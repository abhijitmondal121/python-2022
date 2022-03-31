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



# a=int(input("Enter the value : "))
# sum=0
# for i in range(1,a):
#     if a%i==0:
#         sum+=i

# if sum==a:
#     print("perfect")
# else:
#     print("Not perfect")        


# k=eval(input("enter thew value of the list :"))
# l=list(k)
# nl=[]
# for i in l:
#     if i not in nl:
#         nl.append(i)
# t=tuple(nl)
# print(t)    


# k=eval(input("enter thew value of the list :"))
# l=list(k)

# for i in l:
#    l.remove(i)
#    i=i+2
# t=tuple(l)
# print(t)    

# def armstrong(a):
#     temp=a
#     sum=0
#     c=0
#     while temp!=0:
#         temp//=10
#         c=c+1
#     temp=a

#     while a > 0:
#         r=a%10
#         f=pow(r,c)
#         sum=sum+f
#         a=a//10

#     if temp==sum:
#         print("Armstrong Number :") 
#     else:
#         print("Not Armstrong Number :") 



# def palindrome(a):
#     temp=a
#     rev=0
#     while a > 0:
#         r=a%10
#         rev=rev*10+r
#         a//=10
#     if temp==rev:
#         print("palindrome")
#     else:
#         print(" Not palindrome")



# def perfect(a):
#     sum=0
#     for i in range(1,a):
#         if a%i==0:
#             sum+=i

#     if sum==a:
#         print("perfect")
#     else:
#         print("Not perfect")        



# a=int(input("Enter the value : "))
# armstrong(a)
# a=int(input("Enter the value : "))
# palindrome(a)
# a=int(input("Enter the value : "))
# perfect(a)



# d={1:1,2:2,3:3,4:4,5:5}
# sum=0
# for i in d.values():
#     sum=sum+i
# print(sum)    

# s={}
# n=int(input("Enter the range : "))
# for i in range (0,n):
#     key=input("Enter the key : ")
#     value=input("Enter the value : ")
#     s[key]=value

# key=input("Enter the key : ")
# if key in s.keys():
#     print("present")
# else:
#     print("Not present")    


s1={}
n=int(input("Enter the range : "))
for i in range (0,n):
    key=input("Enter the key : ")
    value=input("Enter the value : ")
    s1[key]=value

s2={}
n=int(input("Enter the range : "))
for i in range (0,n):
    key=input("Enter the key : ")
    value=input("Enter the value : ")
    s2[key]=value

# s3={}
s2.update(s1)
print(s2)