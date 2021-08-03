import arthimetic_functions
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))

A=arthimetic_functions.add(x,y)
B=arthimetic_functions.mul(x,y)
C=arthimetic_functions.sub(x,y)
D=arthimetic_functions.div(x,y)


print("The sum of x and y is:%d"%(A))
print("The product of x and y is:%d"%(B))
print("The substraction of x and y is:%d"%(C))
print("The divison of x and y is:%d"%(D))
