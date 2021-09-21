# for i in range(2):
#     a=int(input("enetr a:"))
#     b=int(input("enter b:"))
#     c=a+b
#     print(c)


l=[]
n=int(input())
for i in range(n):
    x=int(input())
    l.append(x)
def countdup(l):
    a = set(l)
    c = 0
    for i in l:
        if l.count(i) > 1:
            c += 1
    return c
print(countdup(l))

# l=[1,2,3,2,4,2]
# # print(l.count(2))
# c=0
# a=set(l)
# print(a)
# for i in l:
#     if l.count(i)>1:
#         print("yes")
#         c+=1
#         print(c)
#     # print(l.count(i))


# a=10 #global variable
# def something():
#     a=15 #local variable
#     print(f"inside {a}")
# something()
# print(f"outside {a}")
#
# ''' can we use local in global ??'''
#
# a=10 #global variable
# def something():
#     global a
#     a=15 #local variable
#     print(f"inside {a}")
# something()
# print(f"outside {a}")


# class employee:
#     def data(self):
#         print(f"company is:{self.company} age is:{self.age} id is:{self.id}")
# arvind=employee()
# ashu=employee()
# arvind.company="google"
# arvind.age=22
# arvind.salary=100
# ashu.company="intel"
# ashu.age=21
# ashu.salary=20
#
# arvind.data() #employee.data(arvind)


# class employee:
#     salary=500
# arvind=employee()
# ashu=employee()
# arvind.company="google"
# arvind.salary=100
# ashu.company="intel"
# # ashu.salary=200
# print(arvind.salary)
# print(ashu.salary)


# class employee:
#     count=0
#     def __init__(self):
#         # print("good morning!!")
#         employee.count+=1
#
# arvind=employee(age)
# ashu=employee()
# print(employee.count)

# class employee:
#     def data(self):
#         print(f"company is:{self.company} age is:{self.age} id is:{self.id}")
# arvind=employee()
# ashu=employee()
# arvind.company="google"
# arvind.age=22
# arvind.salary=100
# ashu.company="intel"
# ashu.age=21
# ashu.salary=20


# class employee:
#     def __init__(self,age,salary):
#         self.age=age
#         self.salary=salary
#     def data(self):
#         print(f"age is {self.age} salary is {self.salary}")
# arvind=employee(22,100)
# arvind.data()
