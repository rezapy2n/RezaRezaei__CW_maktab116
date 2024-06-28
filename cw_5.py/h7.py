def do_before(func):
    def decorator(wrapped_func):
        def wrapper(*args, **kwargs):
            func()  # Execute the pre-function
            return wrapped_func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage
def pre_func():
    print("Executing the pre-function...")

@do_before(pre_func)
def wrapped_function():
    print("Executing the wrapped function...")

# Call the wrapped function
wrapped_function()