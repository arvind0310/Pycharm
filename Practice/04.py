# # str="arvind"
# # a=str[-6:-2]
# # print(a)
# dict={"name":"arvind","proff":"student","name":"chandu"}
# # print(dict["name"])
# print(dict)

# name=input("enter the name:")
# date=input("enter date:")
# print(f"dear <|{name}|>\nyou are selected!\ndate:<|{date}>|")


# letter='''These letter is written by arvind
# '''
# letter=letter.replace("is","was")
# letter=letter.replace("arvind","chandu")
# letter=letter.replace("chandu","chandan")
# print(letter)

# letter=''' this bad is good '''
# letter=letter.replace("bad","good")
# letter=letter.replace("good","bad")
# print(letter)

# a='''arvind is my name'''
# print(a.endswith("name"))
# print(a.find("i"))
# print(a.count(" "))

# a="arvind \\is my name"
# print(a)
#
# name=input("enetr the name: ")
# date=input("enter the date ;")
# a=f"hii <|{name}|>\ncongrats! you are selected\nyou are selected\n<|{date}|>"
# print(a)

# a=[1,2,3]
# print(a[0])
# a[0]=5
# # print(a[-1])
# print(a)

# t=(5,4,3) // tuple is immutable where list is mutable cz list can be changed
# print(t.count(5))
# y=1,2
# print(y)
# print(type(y))

# f1=input("enetr the fruit 1: ")
# f2=input("enetr the fruit 2: ")
# f3=input("enetr the fruit 3: ")
# f4=input("enetr the fruit 4: ")
# f5=input("enetr the fruit 5: ")
# my_fruit=[f1,f2,f3,f4,f5]
# print(my_fruit)

# a=(1,0,4,0)
# print(a.count(0))


# age=int(input("enter your age :"))
# if age==18:
#     print("kid")
# if age >18:
#     print("adult")
# if age <25:
#     print("less than 25")
# else:
#     print("else")
# print("DONE")








# a = 8
# if(a>6):
#     print("the value is greater than six ")
# if(a>4):
#     print("grtr than 4")
#
# if(a>3): #if elif else ladder start
#     print("the value is greater than three ")
# elif(a>5):
#     print("greater than five ")
# else:
#     print("none")
# print("done")

# a=3
# if a<3:
#     print("less than 3 ")
# elif a==3:
#     print("equal to 3 ")
# else:
#     print('else stat')
#
# name=input('enter the name: ')
# date =input("enter the date:")
# print(f'''hii {name}
# you are selected at {date}''')

# lst=[5,3,2]
# print(max(lst))

# lst=[]
# x=int(input('how many numb ?:'))
# for i in range(x):
#     num=int(input(f"enter the numb {i+1}:"))
#     lst.append(num)
# print(f"max num in these {x} numb is {max(lst)}")
#
#
# text=input("enter your text :")
# if ("fuck" in text):
#     spam=True
# elif 'bitch' in text:
#     spam=True
# else:
#     spam=False
# if(spam):
#      print("its spam")
# else:
#      print("its not spam")
#
# print(text.count("fuck"))

# a=input("enter your string :")
# b=input("enter your searching element:")
# if b not in a:
#     print("word not found")
# else:
#     print("word found")

# list=['a','b','c','d']
# u=input("enter your name:")
# if u in list:
#     print("found")
# else:
#     print("not found")
# l=[1,2,3]
# if 2 in l:
#     print("found")

# i=1
# while i<=50:
#     print(i)
#     i+=1

# list=[1,2,3,4,5,3]
# x=len(list)
# i=0
# while i<x: #while i<len(list)
#     print(list[i])
#     i+=1
#
# list=[1,2,3]
# for i in list:
#     print(i)

# x=int(input("enter the number :"))
# for i in range(1,11):
#     print(f"{x}X{i}={x*i}")
# for i in range(10):
#     if i==3:
#         break
#     print(i)

# for i in range(10):
#     if i==3:
#         continue
#     print(i)
# l=["a",'b','c']
# for i in l:
#     print(i)
#     if i.startswith("a"):
#         print('good morning',i)

# n=int(input('enetr the number :'))
# for i in range (2,n):
#     if n%i==0:
#         print("not prime")
#         break
#     else:
#         print("prime!")
#         break

# n=int(input('enter the num to:'))
# # x=0
# # while n>0:
# #     x=(n*(n+1))/2
# #     # n=n-1
# #     print(x)
# #     break
# sum=0
# while n>0:
#     sum=sum+n
#     n=n-1
# print("sum is :",sum)

# n=int(input('enetr the numb:'))
# fact=1
# while n>0:
#     fact=fact*n
#     n=n-1
# print(fact)

# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# print("1"*5)
# n=4
# for i in range(1,5):
#     print("*"*i)

# n=1
# while n<=4:
#     print("*"*n)
#     n+=1

# n=4
# while n>0:
#     print("*"*n)
#     n=n-1

# for i in range(4,0,-1):
#     print("*"*i)


# for i in range(1,5):
#     print('*'*i)


# n=3
# for i in range (1,4):
#     print(" " *(n-i),end="")
#     print("*" *(2*i-1),end="")
#     print(" " * (n-i))
