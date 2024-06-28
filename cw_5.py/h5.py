def my_range(start, stop, step):

    if not isinstance(start, int) or not isinstance(stop, int) or not isinstance(step, int):
        raise ValueError("All parameters (start, stop, step) must be integers.")
    
    if step == 0:
        raise ValueError("The step parameter cannot be zero.")
    
    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        raise ValueError("The step parameter prevents the sequence from reaching the stop value.")
    
    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step

for num in my_range(1, 10, 2):
    print(num)
