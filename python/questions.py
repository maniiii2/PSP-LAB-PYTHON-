#Lambda function
#We use lambda functions when we require a nameless function for a short period of time. In Python, we generally use it as an argument to a higher-order function .
#Lambda functions are used along with built-in functions like filter() , map() etc.

double = lambda x: x * x

print(double(10))
