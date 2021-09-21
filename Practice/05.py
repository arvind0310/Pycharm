# f=open("sample.txt",'r')
# data =f.read()
# print(data)
# f.close()
#
#
# f=open("another.txt","w")
# f.write("i am appending 3") #it over write the whole text file and replace it by the new content
# f.close()
#
# f=open("another.txt","a")
# f.write("hii i am appending ") # it will append the existing file , the of time you will append the the same it will append
# f.close()

# f=open("sample.txt","r")
# a=(f.read())
# str=input("enter the searching word : ")
# if str in a :
#     print(f"yes its there ")
# # print(a)
# f.close()


# def game():
#     a=int(input("enter your score : "))
#     return a

# score=game()
# with open("another.txt","r") as f:
#     highscore =int(f.read())
# if highscore<score:
#     with open("another.txt","w") as f:
#         f.write(str(score))

# with open("another.txt","r") as f:
#     print(f.read())

# with open("another.txt","a") as f:
# f.write(" 65 is the best ")
#
# n=int(input("enter the num :"))
# def multi(n):
#     for i in range(1,11):
#         if i>0:
#             return (f"{n}X{i}={n * i}")
#
# # print(multi(n))
# with open("table.txt","w") as f:
#     f.write(str(multi(n)))


# f=open("sample.txt","r")
# print(f.read())
# f.close()

# f=open("sakshi.txt","w")
# f.write("hii i am sitting behind you ")
# f.close()
# with open ("table.txt","r") as f:
#     print(f.read())
# for i in range(2,21):
#     with open(f"table/multiplication table of {i}.txt","w") as f :
#         for j in range(1,11):
#             f.write(str(f"{i}X{j}={i*j}\n"))
# with open ("sample.txt","r") as f:
#     content=f.read()
#     if "donkey" in content:
#         with open("sample.txt", "w") as f:
#             content=content.replace("donkey","###")
#             f.write(content)

# words=["donkey","kaddu", "kutta"]
# with open ("sample.txt","r") as f:
#     content=f.read()
#     for word in words:
#         with open("sample.txt", "w") as f:
#             content=content.replace(word,"###")
#             f.write(content)

# with open("sample.txt") as f:
#     content=f.read().lower()
#     # print(content.lower())
# if "A" in content:
#     print("yes")
# else:
#     print("no")
# with open("sample.txt","r") as f:
#     content=f.read()
# with open("copy.txt","w") as f:
#     f.write(content)


## they are identical or not

# with open("sample.txt","r") as f:
#     content=f.read()
# with open("copy.txt","r") as f:
#     content2=f.read()
# if content in content2:
#     print("they are identical")
# else:
#     print("no they are not")
# file1="sample.txt"
# file2="copy.txt"
# with open (file1) as f:
#     f1=f.read()
# with open (file2) as f:
#     f2=f.read()
# # if f1 == f2:
# if f1 in f2 :
#     print("they are itentical")
# else:
#     print("thy are not ")

# with open("sample.txt","w") as f:
#     f.write("")


# import os
# os.remove('sample2.txt')
# import os
# file1="sample2.txt"
# file2="renamed_python_file"
# with open(file1,"r") as f:
#     content=f.read()
# with open(file2,"w") as f:
#     f.write(content)
# os.remove(file1)
# a=int(input("a:"))
# b=int(input("b:"))
# def sum(a,b):
#     return a+b
# print(sum(a,b))
# print(type("6"))
# '''
# PascalCase : EmployeeName,IsInteger
# camelCase: employeeName , isName , isInteger
# '''

# branch={"arvind":"ec","anubhav":"cs"}
# print(branch)
# print(branch["anubhav"])


# class student1:
#     college="abesit"
#
# anubhav=student1()
# # anubhav.branch='cs'
# # anubhav.rollnum="120"
# print(anubhav.college)
