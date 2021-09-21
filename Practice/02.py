# for i in range(10):
#     n=int(input("enter your year : "))
#     if n%4==0 and n%100!=0:
#         print("1 leap year ")
#     elif n%400==0:
#         print("2 leap year ")
#     elif n%100==0:
#         print("3 not leap year  ")
#     else:
#         print("4 not leap year ")

# l=[1,2,3,5,6]
# for i in l:
#     if i%2==0:
#         print('even no is :',i)
# # print(l.count(1))

# l=[2,3]
# print(l)
# l[0]=4
# print(l)

# dict={1:a,2:b}
# print(dict[1])

# s=set()
# s.add(1)
# s.add(2)
# print(s)
# a=(1,2)
# # print(type(a))
# # print(a.count(1))
# x=set(a)
# # print(x)
# for i in x:
#     print(i)

# s={1,2,3}
# s=[1,2,3]
# s=(1,2,3)
# for i in s:
#     print(i)

# dict={}
# dict[0]="zero"
# dict[1]="one"
# dict["two"]=2
# dict["three"]=3
# dict['arvind']='chandu'
# dict["prime num"]=1,3,5,7,11
# print(dict)
#
# l=[1,2,3]
# l.append(2)
# print(l)

# str="aaaa"
# # print(str.count("a"))
# print(str.find('a'))

# a=int(input("enter a :"))
# b=int(input("enter b :"))
# temp=a
# a=b
# b=temp
# print("inverted is : " ,a,b)

# a=int(input("enter a :"))
# b=int(input("enter b :"))
# a,b=b,a
# print("inverted is : " ,a,b)

# a=int(input('enter the numb a'))
# b=int(input('enter the numb b'))
# c=int(input('enter the numb c'))
# d=int(input('enter the numb d'))
# if a>d:
#     f1=a
# else:
#     f1=d
# if b>c:
#     f2=b
# else:
#     f2=c
# if f1>f2:
#     print(f1,"is greatest")
# else:
#     print(f2,'is greater ')
#
# l=[]
# n=int(input("enetr the total numb:"))
# for i in range(1,n+1):
#     x=int(input(f"enter the numb {i} :"))
#     l.append(x)
# print("max numb is",max(l))

# str="chamtkaar pe chamtkaar krnege "
# str1=str.replace("chamtkaar","balatkar ")
# print(str1)
# # s=input("enter your spam word :")
# if "x" in str1:
#     spam=True
# elif "y" in str1:
#     spam=True
# else:
#     spam=False
#
# if spam:
#     print("its spam")
# else:
#     print('not spam')


# def greet(name):
#     print("good morning ",name)
#     # return "good morning"+name
# greet('arvind')
# def sum(x,y):
#     return x+y
# n=sum(3,5)
# print(n)

'''factorial programm'''

# n=4
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# def fact(n):
#     # n = 4
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact
# print(fact(5))

# def fact_rec(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact_rec(n-1)
# f=fact_rec(5)
# print(f)

# def max(n1,n2,n3):
    # if n1>n2 and n3:
    #     great=n1
    # elif n2> (n1 and n3):
    #     great=n2
    # else:
    #     great=n3
    # return great
    # '''OR'''
    # if n1>(n2 and n3):
    #     return n1
    # elif n2> (n1 and n3):
    #     return n2
    # else:
    #     return n3
# print(max(1,2,3))

# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n+sum(n-1)
# n=int(input("eneter the n numb :"))
# x=sum(n)
# print(x)
# def pattern(n):
#     for i in range(n,0,-1):
#         print ("*"*i)
# n=int(input("enetr the numb:"))
# pattern(n)

# str=" its boy gg vysr"
# print(str.replace("gg",""))
#

# x=int(input("enetr the numb:"))
# for i in range(1,x+1):
#     print(f"{x}x{i}={x*i}")

'''wrong'''
# def multi(x):
#     for i in range(1, x + 1)
#         return x*i
#
#     return n
#         # print(f"{x}x{i}={x*i}")
#
# x=int(input("enetr the numb:"))
# print(multi(x))

# for i in range(1,4):
#     x=i*2
#     print(x)

'''very imp '''
# def fun(n):
#     for i in range(1,n):
#         return i # will only iterates ones
# print(fun(5))

# def fun(n):
#     for i in range(1,n):
#         print(i)
# n=int(input("enetr the nunb: "))
# print(fun(n))




# import random
# a=random.randint(1,3)
# print(a)
''' snake water gun:
snake > water
water>gun
gun> snake
'''
# import random
# def gamewin(comp,you): #you lossed or won
#     if comp==you:
#         return None
#     elif comp=="s":
#         if you=="w":
#             return False #you lossed
#         if you=="g":
#             return True
#     elif comp == "w":
#         if you == "g":
#             return False
#         if you == "s":
#             return True
#     elif comp=="g":
#         if you=="s":
#             return False
#         if you=="w":
#             return True
#
# print("comp turn : snake(s) water(w) or gun(g)?:")
# n=random.randint(1,3)
# if n==1:
#     comp="s"
# elif n==2:
#     comp="w"
# elif n==3:
#     comp="g"
# you=input("enter your choise : snake(s) water(w) or gun(g)?:")
#
# a=gamewin(comp,you)
#
# print(f"comp chose : {comp} and you chose : {you}")
# if a==None:
#      print("its a Tie")
# if a==True:
#     print("you won")
# if a==False:
#     print('you lossed')

# n=int(input("enetr numb:"))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
#
#     else:
#         print("prime")

# def add_sub(x,y):
#     c=x+y
#     d=x-y
#     return c,d
# r1,r2=add_sub(5,4)
# print(r1,r2)

# a=3
# a=5
# print(a)

# def update(x):
#     x=8
#     print(x)
# a=10
# update(a)
# print(a)

# def update(lst):
#     lst[1]=10
#     print(lst)
# lst=[1,2,3,4,5]
# print(lst)
# update(lst)
# print(lst)
# def sum(*b):
#     c=0
#     print(b)
#     for i in b:
#         c=c+i
#     # print(c)

#     return c
#
# 
# print(sum(1,2,3,4,5))
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.items()


#
# dict={"apple":"seb","boy":"ladka"}
# for i,j in dict.items():
#     print(i,j)

# print(dict)
# print(dict.items())
# print(dict.get())
# a=input("enetr the eng word:")
# print(dict.get(a))

# def update(x):
#     lst[1]=5
#     print(lst)
#
# lst=[1,2,3]
# update(lst)
# print(lst)

#
# def update(x):
#     x=3
#     print("x:",x)
#
# a=5
# update(a)
# print("a:",a)


# dict={"a":1,"b":2}
# for i,j in dict.items():
#     print(i,j)
print(dict.items())
# for i in range(4):
#
#     text=input("enter the text: ")
#     if("ugly" in text):
#         print(text.replace("ugly","@###"))
#     elif("pig" in text):
#         print(text.replace("pig","@###"))
#     elif("fat" in text ):
#         print(text.replace("fat","@###"))

# text=input()
# if("ugly" in text):
# 	print(text.replace("ugly","@###"))
# elif("pig" in text):
# 	print(text.replace("pig","@###"))
# elif("fat" in text ):
#  	print(text.replace("fat","@###"))

# lst=[]
# x=int(input("How many nums?:"))
# for i in range(x):
#     # num=int(input("enter the number"+str(i+1)+":"))
#     num = int(input(f"enter the number{i+1}:"))
#     lst.append(num)
# print("the max value is ",max(lst))
# lst=[]
# x=int(input("enter the number of fruits: "))
# for i in range(x):
# 	f=input(f"enter the fruit {i+1}:")
# 	lst.append(f)
# print(f"list of fruits are {lst}")


