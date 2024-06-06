def is_power_of_base(number, base):
     if number < 1 or base <= 1:
         return False

    while number > 1:
         if number % base != 0:
             return False
         number /= base

    return True
test_number = int(input("enter the number: "))
test_base = int(input("enter the power number: "))
result = is_power_of_base(test_number, test_base)
print(f"Is {test_number} a power of {test_base}? {'Yes' if result else 'No'}")