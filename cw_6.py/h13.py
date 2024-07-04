class MathUtil:
    @classmethod
    def is_prime(cls, num):
        
        if num <= 1:
            return False  

       
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False  

        return True  
    
number_to_check = 25
if MathUtil.is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")
