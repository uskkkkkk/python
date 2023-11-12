import time

def memoize(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        return result
    
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    
    return wrapper


def timer(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        return (f"{func.__name__}: "
                f"argument: {args[0]} "
                f"time: {execution_time}")

    return wrapper


@timer
@memoize
def fibonacci_memoize(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@timer
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci_memoize(20))
print()
print(fibonacci(20))
