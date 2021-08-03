#A Dictionary in python is the unordered and changeable collection of data values that holds key-value pairs.
#A Dictionary in python is declared by enclosing a comma separated list of key-value pairs using curly braces({}).
#syntax or python Dictionary

'''
student1={'Name':'manikanta','branch':'ECE','section':'A1','Roll_no':23}
print(type(student1))
print(student1)

student1={'Name':'manikanta','branch':'ECE','section':'A1','Roll_no':23,'Name':'surya'}
print(student1)


student1={'Name':'manikanta','branch':'ECE','section':'A1','Roll_no':23}
print(student1['Roll_no'])



student1={'Name':'manikanta','branch':'ECE','section':'A1','Roll_no':23}
print("Before updating")
print(student1)
#'Member':'NCC'

student1.update({'Member':'NCC'})
print('After updating')
print(student1)


#delete keys from the Dictionary
student1={'Name':'manikanta','branch':'ECE','section':'A1','Roll_no':23,'Member':'NCC'}
print("Before deleting")
print(student1)
del student1['section']
print("After deleting")
print(student1)

print(student1.items()) #it will print list of tuple pairs
'''

student1={'Name':'manikanta','branch':'ECE','section':'A1','Roll_no':23,'Member':'NCC'}
print(student1.values())
print(student1.keys())
#print("keys of student1 are")
#print(student1.keys())
























