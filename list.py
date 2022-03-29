# l=eval(input("enter thew value of the list :"))
# n=len(l)
# # list=l[4:n]
# # print(list)
# # print(l[-5])
# # list=l[2:n:2]
# # print(list)


# sum=0
# m=int(input("enter 1st element:"))
# n=int(input("enter 2nd element:"))

# for i in l:
#     if i%m==0 and i%n==0:
#         print (i) 

   
l=eval(input("enter thew value of the list :"))

for i in l:
    for j in range(i): 
        if i==j:
            l.remove(j)
print(l)             


# search

# l=eval(input("enter thew value of the list :"))
# m=int(input("enter 1st element:"))
# f=0
# for i in l:
#     if(i==m):
#         print("present")
#         f=1
# if f==0 :
#     print("Not present")            

     