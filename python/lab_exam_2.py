

#9.sum and average in a list

number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)


def sum_of_list(l,n):
  if n == 0:
    return l[n];
  return l[n] + sum_of_list(l,n-1)

print("The sum of my_list is", sum_of_list(number_list,len(number_list)-1))

def Average(l): 
    avg = sum(l) / len(l) 
    return avg
  

average = Average(number_list) 
  
print("Average of my_list is", average)
