def is_perfect_number(n):
     if n < 2:
         return False

     sum_of_divisors = 1
     for i in range(2, int(n**0.5) + 1):
         if n % i == 0:
             sum_of_divisors += i
             if i != n // i:
                 sum_of_divisors += n // i

     return sum_of_divisors == n

test_number = int(input("enter number: "))
result = is_perfect_number(test_number)
print(f"Is {test_number} a perfect number? {'Yes' if result else 'No'}")