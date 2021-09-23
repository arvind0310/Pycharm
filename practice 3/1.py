
l=[1,1,2,1,3,3,3]
for i in range(len(l)): #after 3 time ..no 3 will be there in list
    l.remove(3)
print(l)

#errror


l=[1,1,2,1,3,3,3]
for i in range(l.count(3)):
    l.remove(3)
print(l)
