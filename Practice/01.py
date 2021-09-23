# a=input("enter Your name:")
# print("good morning,"+a)
# print(f'good morning {a}')

# name =input("enter the name:")
# date=input("enter the date:")
# letter=f'''dear {name}
# you are selected!
# date:{date}'''
# print(letter
# print(f"dear {name} you are selected!\n"
#       f"date:{date}")
# letter=letter.replace("<|name|>",name)
# letter=letter.replace("<|date|>",date)
# print(letter)
#
# str="this is double space  "
# str1=str.replace("  "," ")
# print(str1)
#
# str1='''Peechle buttis saal se inhone nirantar is college mein chamatkar pe chamatkar kiye.
# Umeed hai aagey bee karte rahenge Hamein to aashcharya hota hai ki ek insaan apne jeevan kaal
# mein itni chamatkar kaisi kar sakta hai'''
# str= str1.replace("chamatkar","balatkar")
# print(str)

# letter="hii arvind\n\tyou are good !\nthanks !"
# print(letter)
# a=[0,1,2,3,4,5,6]
# print(a[:5]) #from 0 to less than 5th index
# print(a[0])
# print(a[-7])
# print(a[0:5])
#
# print(a[2:]) #onwards 2nd index
# print(a[1:5])
# print(a[-1])
# print(a[-1:]) #onwards from -1th index ( here 6 only)

# print(a[-2:]) #onwards from -2nd index
#
# print(a[:-1]) # from 0 till before -1th index

# str="Arvind"
# print(str[-4:-1])
# print(str[-6])
# # print(a[:-1])

# a=[1,2,3,4,5,6,8,7]
# # a.sort()
# a[1]=8
# a.sort()
# print(a)
# tup=(1,2,3)
# print(tup[0:2])

# str="ABCD"
#
# print(str.count("A"))
# print(str.find("B"))
# l=[1,2,3,4,5]
# print(len(l))



# t1=()
# t1=(1,5)
# print(t1)
# f1=input("enter the fruit1:")
# f2=input("enter the fruit2:")
# f3=input("enter the fruit3:")
# f4=input("enter the fruit4:")
# f5=input("enter the fruit5:")
# f6=input("enter the fruit6:")
# f7=input("enter the fruit7:")
# my_fruit=[f1,f2,f3,f4,f5,f6,f7]
# print(my_fruit)
# # print(f"[{f1},{f2},{f3},{f4},{f5},{f6},{f7}]")
# # print(f"hii this is {f1} my fav food")
# # print(my_fruit)
# my_fruit[1]="b"
# print(my_fruit)
# m1=int(input("enter the marks1:"))
# m2=int(input("enter the marks2:"))
# m3=int(input("enter the marks3:"))
# m4=int(input("enter the marks4:"))
# m5=int(input("enter the marks5:"))
# m6=int(input("enter the marks6:"))
# m=[m1,m2,m3,m4,m5,m6]
# m.sort()
# print(m)
# a=(7,0,8,0,0,9)
# print(a.count(0))
# dict={"a":1,"b":2,'c':3,1:2,2:"arvind"}
# print(dict["a"])
# dict['a']=4
# print(dict)
# dict={"a":1,"b":2,'c':3,1:2,2:"arvind"}
# print(dict)
# a={"arvind":1,"chandu":2}
# b= dict.update(a)
# # print(dict)
# b=set()
# print(type(b))
# b.add(5)
# b.add(6)
# print(b)
# s={1,2,3,4,5}
# i=s.intersection({3,4})
# print(i)
# mydict={'seb':"apple","ladka":"boy","billi":"cat"}
# # print(mydict.get("seb"))
# # print(mydict["billi"])
# print(mydict.keys())
# a=input("enter your hindi word\n")
# # print("your english is:",mydict[a])
# print("your english is:",mydict.get(a))


# num1=int(input("enter the 1 number :"))
# num2=int(input("enter the 2 number :"))
# num3=int(input("enter the 3 number :"))
# num4=int(input("enter the 4 number :"))
# num5=int(input("enter the 5 number :"))
# num6=int(input("enter the 6 number :"))
# num7=int(input("enter the 7 number :"))
# num8=int(input("enter the 8 number :"))
# s={num1,num2,num3}
# print(s)

# a={18,"18"}
# print(a)

# s=set()
# s.add(20)
# s.add(20)
# s.add(20)
# s.add(20)
# s.add(20)
# s.add(20.0)
# s.add(20.0)
# s.add(20.0)
# s.add(20.0)
# s.add("20")
# s.add("20")
# s.add("20")
# s.add("20")

# print(s)
# print(len(s))
#
# dict={}
# dict.add(5)
# print(dict)

# d={"a":1}
# d['a']=2
# print(d)

'''
adding values in empty set vs dict
'''

#dict

'''https://www.geeksforgeeks.org/python-dictionary/#:~:text=Dictionary%20can%20also%20be%20created,placing%20to%20curly%20braces%7B%7D.'''

# dict={}
# dict[0]="zero"
# dict[1]="one"
# dict["two"]=2
# dict["three"]=3
# dict['arvind']='chandu'
# dict["prime num"]=1,3,5,7,11
# print(dict)
# print(dict.get("three"))

#set

# s=set()
# s.add("arvind")
# s.add("chandu")
# s.add(1)
# print(s)

'''set take randomly object inside it '''

#list

# lst=[]
# lst2=1,2
# lst.append(lst2)
# print(lst)
# lst=[]
# lst.append(1)
# lst.append(2)
# lst.append(5)
# # lst.insert(0,'a')
# lst[0]="a"
# print(lst)
# lst.remove(5) #...remove that element
# print(lst)

# favlang={"a":"python",'b':"python","c":"c#", "d":"c++ "}
# print(favlang)

# favlang = {}
# a=int(input("enter your fav language Arvind"))
# b=int("enter your fav language chandu")
# c=int("enter your fav language sakshi")
# d=int("enter your fav language adamya")
#
# favlang['arvind']=10
# favlang["anuj"]=12
# print(favlang)
# favlang["chandu"]=21
# print(favlang)

# keys=["arvind","abhay","amit"]
# values=[15,9,7]
# school=dict(zip(keys,values))
# print(school)
# school['dharmesh']=8
# print(school)

##we can use list in dict
# branch={'arvind':"ec","anubhav":"cs","vaibhav":['cs',"it"]}
# # print(branch)
# # print(branch['vaibhav'][0])
# print(branch.values())

# b=5
# c=6
# d=complex(b,c)
# print(d)
# a=5
# b=6
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

# if-elif-else ladder
# a = 8
# if(a>6):
#     print("the value is greater than six ")
# if(a>4):
#     print("grtr than 4")
# if(a>3):
#     print("the value is greater than three ")
# elif(a>5):
#     print("greater than five ")
# else:
#     print("none")
# print("done")
''' if if if me sab check hogaa 
jaise hi if ke just ke baad elif aaya treat as if elif ab elif me tabhi enter when uske oopar vaala g'''

# age=int(input("enter the age :"))
# if (age>18 and age<35):
#     print("adult")
# else:
#     print("not adult")

# print("hello rajan welcome")
# a=int(input("enetr the nummber 1 : "))
# b=int(input("enter the second number 2:"))
# print("your addition is :", a+b)

# a=5
# if(a is 5):
#     print("yes")
# else:
#     print("no")
# a = 5
# if (a==5):
#     print("yes")
# else:
#     print("no")
# a=[4,5,6]
# for i in range(4):
#     print(i)

# a=int(input("enter the num a:"))
# b=int(input("enter the num b:"))
# c=int(input("enter the num c:"))
# d=int(input("enter the num d:"))
# if(a>d):
#     f1=a
# else:
#     f1=d
# if(b>c):
#     f2=b
# else:
#     f2=c
# if(f1>f2):
#     print(f1,'is greatest')
# else:
#     print(f2,"is greatest")

# lst=[]
# x=int(input("How many nums?:"))
# for i in range(x):
#     # num=int(input("enter the number"+str(i+1)+":"))
#     num = int(input(f"enter the number{i+1}:"))
#     lst.append(num)
# print("the max value is ",max(lst))


# sub1=int(input("enter the marks of sub1 :"))
# sub2=int(input("enter the marks of sub2 :"))
# sub3=int(input("enter the marks of sub3 :"))
# per=(sub1+sub2+sub3)/3

# if(sub1<33 or sub2<33 or sub3<33):
#     print("you are failed due to ess marks in sub")
#
# # print("your percent is :",per)
# elif(per<=40):
#     print('the student is failed due to per less than 40')
# else:
#     print("you have pass the exam with the per",per,"%")


##spam detector

# text=input("enter the text\n")
# if("fuck" in text):
#     spam=True
# elif("bitch" in text):
#     spam=True
# elif("whore" in text ):
#     spam=True
# else:
#     spam=False
# if(spam):
#     print('this is spam')
# else:
#     print('this is not spam')

# for i in range(5):
#     print(i+1,end='')
# a="hii its arvind "
# # print(a)
# print(a.strip(a))


##


# a=input("enter the user name :\n")
# print(len(a))
# if(len(a)>10):
#     print("length is greater than 10")
# else:
#     print("less than 10")

##
#
# a=input("enter your string :\n")
# b=input("enter your word:")
# if(b not in a):
#     print("word not found")
# else:
#     print("word found ")

# a=input("enter your string :\n")
# b=input("enter your word:")
# if(b in a):
#     print("word found")
# else:
#     print("word not found ")


# username=["arvind","adamya","ashee","sakshi"]
# a=input("enter your username :")
# if(a in username):
#     print("username found!!")
# else:
#     print("username not found")

# marks=int(input("enter your marks :"))
# if marks>=90:
#     grade="ex"
# elif marks>=80:
#     grade="a"
# elif marks>=70:
#     grade="b"
# elif marks>=60:
#     grade="c"
# elif marks>=50:
#     grade="d"
# else:
#     grade="f"
# print('your grade is: ' +grade+" broda")

# a=input("enter your post: ")
# b=input("enter the celeb: ")
# if(b in a):
#     print("yes this post is talking about "+b)
# else:
#     print("npp")

######LOOP

# i=0
# while(i<10):
#     print("yes "+str(i))
#     # print("yes",i,"hi")
#     i=i+1
# i=1
# while(i<=50):
#     print(i,end="")
#     i=i+1

# student=["arvind","ashee","adamya","sakshi"]
# # i=0
# # while(i<len(student)):
# #     print(student[i])
# #     i=i+1
# #
# for i in student:
#     print(i," " ,end='')
# for i in range(1,7,8):
#     print(i)

# for letter in 'Python':
#     print('Current Letter :', letter)
#     if letter == 'h':
#       break
#
# print("bye")



# for i in range(10):
#     if i%2!=0:
#         continue
#     print(i)

# a=int(input("enter the number :"))
# for i in range(1,11):
#     # print(a,"*",i,"=",a*i)
#     print(f"{a}x{i}={a*i}")
#
#
# l1=["arvind","shashi","shubham","chandu"]
# for name in l1:
#     print(name)
#     # if name.startswith("s"):
#     #     print("Good Morning!!",name)

# a="hii this is arvind"
# if(a.startswith("h")):
#     print("hii")

# num=int(input("enter the number :"))
# a=1
# while(a<=10):
#     # print(f"{num}x{a}={num*a}")
#     print(num,"x",a,"=",num*a)
#     a=a+1


# a=int(input("enter your num: "))
# for i in range(2,a):
#     if(a%i==0):
#         print("not prime")
#         break
#     else:
#         print("prime")
#         break

# n=int(input("enter the number up to : "))
# while(n>0):
#     print("your sum is :",(n*(n+1))/2)
#     break
# sum=0
# while(n>0):
#     sum=sum+n
#     n=n-1
# print(sum)


# n=int(input("enter the num :"))
# fact=1
# if n>0:
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# elif(n==0):
#     print(f"the fact of {n} is 1")
# else:
#     print("fact is not define ")

# n=int(input("enter the num :"))
# sum=0
# while(n>0):
#     sum=sum+n
#     n=n-1
# # print(sum)
# for i in range(1,4):
#     print("*"*(i))


# n=int(input("enter the num: "))
# for i in range(10,6,-1):
#
#     # print(f'{n}x{i}={n*i}')
#     print(i)

# n=[1,3,3]
# print(sum(n))

# def greet(name):
#     gr="hello"
#     return gr
# a=greet("arvind")
# print(gr)

# def fact(n):
#     pro=1
#     for i in range(1,n+1):
#         pro=pro*i
#     return pro
# n=int(input("enter the numb:"))
# print(fact(n))

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# x=int(input("enter the num :"))
# print(fact(x))

# a=int(input("enter the num a: "))
# b=int(input("enter the num b: "))
# c=int(input("enter the num c: "))
# if(a>b and a>c):
#     print(a,"is greater ")
# elif(b>a and b>c):
#     print(b, " is greater ")
# else:
#     print(c,"is greater ")
#
# lst=[1,2,5]
# print(max(lst))
# print(max(4,5,6))
# lst=[]
# x=int(input("how many num : "))
# for i in range(1,x+1):
#     num=int(input(f"enter your num {i} : "))
#     # num=int(input("enet your number"+str(i)+":"))
#     lst.append(num)
# print("your maximum value is :",max(lst))

# def maximum(n1,n2,n3):
#     if n1>n2 and n1>n3:
#       return n1
#     elif n2>n1 and n2>n3:
#         return n2
#     else:
#         return n3
# n1=int(input("enter the number 1:"))
# n2=int(input("enter the number 2:"))
# n3=int(input("enter the number 3:"))
# print(f"the maximum value is : {maximum(n1,n2,n3)}")
#

# def farh(cel):
#     return (cel*(9/5))+32
# cel=int(input("enter the cel value : "))
# print(f"the far value of {a} is : {farh(cel)}")
#


#recursion python:where function repeat itself


# def fact(n):
#     if n==0 or n==1 :
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))
#
# def sum(n):
#     # if n==1:
#     #     return 1
#     # else:
#         return n+sum(n-1)
# n=int(input("enter the num :"))
# print(f"the sum is {sum(n)}")

# def conv(n):
#     return n*2.54
# n=int(input("enter the num : "))
# print(f"the inch to cem is {conv(n)}")

# string="arvind is a good boy"
# print(string.replace("arvind"," chandu"))

# def remov(string,word):
#     return string.replace(word," ")
# string=input("enter your string here :")
# word=input("enter your word :")
# print(remov(string,word))

#wrong


# def multi(n):
#     for i in range(1,n+1):
#         return i*n
# n=int(input("enter the num :"))
# print(multi(n))

# #correct
# def multi(n):
#     for i in range(1,11):
#         print(f"{n}X{i}={n*i}")
# print(multi(5))

# def multi(n):
#     for i in range(1,11):
#         print(f"{n}x{i}={n*i}")
#         if i==10:
#             continue
#
# n=int(input("enter the num n: "))
# print(multi(n))

# dict={"apple":"seb","ball":"gend","cat":"billi"}
# print(f"your english words are: {dict.keys()}")
# n=input("ente the english word :")
# print(f"hindi of {n} is {dict.get(n)}")
# # print(dict.get("apple"))

# import random
# a=random.randint(1,3)
# print(a)
# import random
#
# def game(comp,you):
#     if comp==you:
#         return None
#     elif comp=="s":
#         if you=="w":
#             return False
#         elif you=='g':
#             return True
#     elif comp=="w":
#         if you=='s':
#             return True
#         elif you=="g":
#             return False
#     elif comp=="g":
#         if you=='w':
#             return True
#         elif you=="s":
#             return False
#
#
# n=random.randint(1,3)
#
# print(f"comp turn : snake(s) water(a) or gun(g) : ")
# if n==1:
#     comp="s"
# elif n==2:
#     comp="w"
# elif n==3:
#     comp="g"
#
# you=input(" yours turn :snake(s) water(a) or gun(g) ?:")
# a=game(comp,you)
# print(f"comp chose {comp}")
# print(f"you chose {you}")
#
# if a==None:
#     print('its a tie ')
# elif a:
#     print("you win ")
# else:
#     print("you loose")

# def fun(a="arvind"):
#     print(a)
# fun()
