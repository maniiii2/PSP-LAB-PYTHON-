students = ["charan","suman","praveen","arsh","ravi"]
student_info = ["charan",10,9.5,"ECE",["chem","phy","maths"]]
'''
print(type(students))
print(students)
print(type(student_info))
print(student_info)


#list slicing

#print(students[0:4])
#print(students[:4])
#print(students[2:-1])
#print(student_info[-1])

#print(student_info[-1][1])
#print(student_info[-1][2])
print(student_info[-1][0:2])



#appending list elements

students.append("venkat")
print(students)


#modification of list
students[1] = "anil"
print(students)




#length of a list

#print(len(students))


#Removing an element from the list

students.pop(3)
print(students)



#find index value of an element

surya_index = students.index("surya")
print(surya_index)
'''

for element in students:
    print(element)
















































