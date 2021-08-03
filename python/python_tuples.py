'''
Tuples are identical to lists in all respects , except for the following properties:
1. Tuples are defined by enclosing the elements in parenthesis( () ).
2. Tuples are immutable.


# Defining a tuple
student =("chandu","ramesh","ramu","tarak","tejas")
print(type(student))
for i in student:
    print(i)


student =("chandu","ramesh","ramu","tarak","tejas")
#print(type(student))
#student[3] ="manikanta"
#print(student)
print(student[0:3])

#what are the benfits of using tuples instead of lists in python

student =("chandu","ramesh","ramu","tarak","tejas")#tuple packing

(s1,s2,s3,s4,s5)= student #tuple unpacking
print(s1)
#print(student)
#print(s2)
#print(s5)

'''

student =("chandu","ramesh","ramu","tarak","tejas")
student_1 =("chandu","ramesh",("ramu","tarak"),"tejas")
#print(type(student_1))
#print(student_1)

#print(student_1[2][0])
 
#print(len(student))
print(len(student_1))

























