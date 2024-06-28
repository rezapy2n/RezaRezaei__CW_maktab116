from functools import reduce

def multiply_numbers(numbers):

  return reduce(lambda x, y: x * y, numbers)

numbers_list = [8, 2, 3, -1, 7]
result = multiply_numbers(numbers_list)
print(f"The product of the numbers in the list is: {result}")
   
   
   
   
 
 # روش دوم 

#import operator
#import functools
#list1 = [8,2,3,-1,7]
#print(functools.reduce(operator.mul,list1))
