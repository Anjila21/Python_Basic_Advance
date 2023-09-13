#There two types of loop.They are
#for loop and while loop
import numpy as np
#While loop
a=10
while(a>1):
    print(a)
    a=a-1

#for loop
name= ["Anjila","Manjila","Manjil"]
for x in name:
    print(x)

#for loop to print marks of students
marks = [10,25,30,23,11,23]
percentage = []
for i in marks:
    percentage.append((i/40)*100)
print(percentage)