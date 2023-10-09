def timer(func):
    """
    Decorator function that times the execution of the input function.
    :param func: A function to be timed.
    :type func: function
    :return: A wrapper function that prints the time taken to execute the input function.
    :rtype: function
    """
    
    import datetime
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        print(datetime.datetime.now() - start)

    return wrapper


def debug(func):
    """
    A decorator function that returns a wrapper function which calls the input `func` with the given `args` and `kwargs`. 
    After calling the function, it prints the name of the function, execution time, arguments passed, and the return value if any. 
    If the function call results in an exception, it prints the name of the function, execution time, arguments passed, and the exception that was raised. 
    The wrapper function does not return any value.
    """

    import time
    import traceback

    def wrapper(*args, **kwargs):
        try:
            start = time.time()
            ret = func(*args, **kwargs)
            print(f'Function {func.__name__} was called taking up {time.time() - start} seconds with {args} and {kwargs} and returned: {ret}')
            print('////////////////////////////')

        except Exception as e:
            print(f'Function {func.__name__} was called  taking up {time.time() - start} seconds with {args} and {kwargs} and crashed with: {traceback.format_exc()}')
            print('////////////////////////////')
    
    return wrapper

def logs(func):
    """
    This function is a decorator that logs the execution time, arguments, and return value or exception 
    of the decorated function to a file called 'log.txt'. It takes any function as input and returns a 
    new function which logs the information upon each call. The function is called with arbitrary positional 
    and keyword arguments and returns the same return value as the decorated function. If the decorated function 
    raises an exception, the exception message is logged instead of the return value.
    """

    import time
    import traceback

    def wrapper(*args, **kwargs):
        with open('log.txt', 'a') as f:
            try:
                start = time.time()
                ret = func(*args, **kwargs)
                print('////////////////////////////', file=f)
                print(f'Function {func.__name__} was called taking up {time.time() - start} seconds with {args} and {kwargs} and returned: {ret}', file=f)
            except Exception as e:
                start = time.time()
                ret = func(*args, **kwargs)
                print('////////////////////////////', file=f)
                print(f'Function {func.__name__} was called taking up {time.time() - start} with {args} and {kwargs} and crashed with: {traceback.format_exc()}', file=f)
    return wrapper
