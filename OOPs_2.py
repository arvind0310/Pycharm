# def fun(name):
#     print(x,name)
#     print("hello")
# x = int(input("enetr x:"))
# fun("arvind")

# a=16
# print(a.bit_length())
#
# l=[1,2,3]
# # l.append(4)
# l.pop()
# print(l)

# class railwayform:
#     def printdata(self):
#         print("hiii")
#         print(f" name is:{self.name} and age is :{self.age}")
# arvindsapp=railwayform()
# arvindsapp.name='arvind'
# arvindsapp.age='22'
# arvindsapp.printdata()


''' class attribute '''

# class employee:
#     company="google"   ##making class atrribute
# # print(employee.company)
#
# arvind=employee()
# ashu=employee()
# print(arvind.company)
# print(ashu.company)
#
# employee.company="youtube"  #changed the class atributes
# print(arvind.company)
# print(ashu.company)

''' obejct(instance) attribute '''

# class employee:
#     company="youtube"
#     salary=100
#
# arvind=employee()
# ashu=employee()
# arvind.company="google"   #making object atrribute
# arvind.salary=300
#
# ashu.company="google "    # ,,,,,,,
# ashu.salary=300
#
# print(arvind.company)
# print(arvind.salary)
# print(ashu.company)
# print(ashu.salary)

''' prefrence is always given to instance attribute over class attribute
 when object attribute is not present then it will take class attribute'''
#
# class employee:
#     company="youtube"
#     salary=100
#
# arvind=employee()
# ashu=employee()
# arvind.company="google"   #making object atrribute
# # arvind.salary=300       #now yaha class attribute used hogaaa
#
# # ashu.company="google "    # ,,,,,,,
# ashu.salary=300
#
# print(arvind.company)
# print(arvind.salary)  #will print class attribute
# print(ashu.company)   #will print class attribute
# print(ashu.salary)

# print(ashu.address)
# will through an error cz pahle object attribute me dhoondha
# fir class attribute me jake dhoondha not found anywhere

# class employee:
#     def data(self):
#         print(f'company is {self.company} and salary is {self.salary}')
#
#
# arvind=employee()
# ashu=employee()
# arvind.company="google"
# arvind.salary=40
# ashu.company="youtube"
# ashu.salary=45
# arvind.data() # employee.data(arvind)
# ashu.data()   # employee.data(ashu)

# class ec:
#     def data(self,rollno,hieght):
#         print(f"age is {self.age} and roll no is  is  {rollno} and hieght is {hieght}")
#
#     @staticmethod
#     def greet():
#         print("good morning")
#
#
#
# arvind=ec()
# ashu=ec()
# arvind.age=22
# ashu.age=21
# arvind.data(19,5.5)
#
# arvind.greet()


'''  giving attribute to the obect '''

# class employee:
#     def __init__(self):
#         print("hiii")
#
# arvind=employee()
# ashu=employee()

# class employee:
#     def data(self):
#         print(f"age is: {self.age} company is: {self.company} roll no is: {self.rollno}")
#
#
# arvind=employee()
# arvind.age=22
# arvind.company='google'
# arvind.rollno=18
# arvind.data() #employee.data(arvind)

''' method 2 '''

# class employee:
#     def __init__(self,age,company,rollno):
#
#         self.age=age
#         self.company=company
#         self.rollno=rollno
#     def getdata(self):
#         print(f"age is: {self.age} company is: {self.company} roll no is: {self.rollno}")
#
#
#
# arvind=employee(22,"google",19)
# # ashu=employee(21,"youtube",20)
#
# arvind.getdata()
# ashu.getdata()


'''method 3: without __init__ '''
# class employee:
#     def getdata(self,age,company,rollno):
#         print(f"age is: {age} company is: {company} roll no is: {rollno} thanks from {self.country}")
# arvind=employee()
# arvind.country="india"
# # ashu=employee()
# arvind.getdata(22,"google",19)
# # ashu.getdata(21,"youtube",20)


''' to access class instance use : {class.instance}'''
# class person:
#     count=0
#     def __init__(self):
#         # print(person.count) to acess class instance
#         person.count+=1
#
# p1=person()
# p2=person()
# print(person.count)

'''inheritance'''

'''single level'''

#class A:
# pass

# a=A()
# a.feature1()
# a.feature2()
# b=B()
# b.feature1()
# b.feature3()
#
''' multilevel '''
#
# class A:  #grand parent class
#     def feature1(self):
#         print("feature1 is working..")
#     def feature2(self):
#         print("feature2 is working..")
# class B(A): #parent class
#     def feature3(self):
#         print("feature3 is working..")
#     def feature4(self):
#         print("feature4 is working..")
# class C(B): #child class
#     def feature5(self):
#         print("feature5 is working..")
# a=A()
# a.feature1()
# a.feature2()
# b=B()
# b.feature1()
# b.feature3()
# c=C()
# c.feature5()
# c.feature1()

''' multiple '''
#
# class A:
#     def feature1(self):
#         print("feature1 is working..")
#     def feature2(self):
#         print("feature2 is working..")
# class B:
#     def feature3(self):
#         print("feature3 is working..")
#     def feature4(self):
#         print("feature4 is working..")
# class C(A,B):
#     def feature5(self):
#         print("feature5 is working..")
# c=C()
# c.feature3()
# c.feature1()
# b=B()
# b.feature3()
