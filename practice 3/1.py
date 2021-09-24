
l=[1,1,2,1,3,3,3]
for i in range(len(l)): #after 3 time ..no 3 will be there in list
    l.remove(3)
print(l)

#errror

#____________________________________+______________________________________________________________________________+___________________________________


l=[1,1,2,1,3,3,3]
for i in range(l.count(3)):
    l.remove(3)
print(l)

#____________________________________+______________________________________________________________________________+___________________________________

n1=int(input("n1:"))
n2=int(input("n2:"))
l1=[]
l2=[]

for i in range(n1):
    x=int(input("element: "))
    l1.append(x)
s1=set(l1)

for i in range(n2):
    y=int(input("element: "))
    l2.append(y)
s2=set(l2)

s3=s1.intersection(s2) #will give common number among both given list
print(s3)
