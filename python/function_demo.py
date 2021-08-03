'''
a function in python is a piece of code which runs when it is referenced.
it is used to utilize the code in more than one place in a program. in-buit functions,user defined functions
print(),input()


def add(x,y):
    return x+y
def multiplication(x,y):
    return x*y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y


x=3
y=4

#print(add(x,y))
#print(multiplication(x,y))
#print(sub(x,y))
#print(div(x,y))

def square(x):
    return x*x
print(square(20))

#Lambda function: It is an anonymous or a function having no name.
#It is a small and restricted function having no more than one line.

#lambda p1,p2:expression

adder = lambda x,y:x+y
print(adder(1,2))

import math
euclidian_distance= lambda x,y: math.sqrt((x**2)+(y**2))
print(euclidian_distance(3,4))

#map()-->It is used to apply a particular operation to every element in a sequence.
even_list=[2,4,6,8,10]
squared_even_list= map(lambda x:x*x,even_list)
print(list(squared_even_list))



#c=[39.2,36.5,37.3,38,37.8] is a list containing temperature values in degree celcius.

#Using lambda function convert the above list into a list of farenheit.

import math
celicius = [39.2,36.5,37.3,38,37.8]

farenheit =map(lambda x:((x*9/5+32),celicius)
print(list(farenheit))



#lambdas.in reduced()

from functools import reduce
even_list = [2,4,6,8,10]
#product = reduce(lambda x,y:x*y,even_list)
#print(product)
#add = reduce(lambda x,y:x+y,even_list)
#print(add)
sum_sqaure = lambda a,b,c,d,e:((a*a)+(b*b)+(c*c)+(d*d)+(e*e)),even_list
print(sum_sqaure)


'''

#Recursion

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))



#write a recursive python function that returns the sum of the first n integers.

def sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(n+sum(n-1))
print(sum(3))


















































