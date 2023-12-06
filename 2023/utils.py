import time 

def time_decorator(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        time_start = time.perf_counter()
        func_ret = func(*args, **kwargs)
        time_end = time.perf_counter()
        print(f"Time spent in {func.__name__}: {time_end - time_start :.12f} s")      
        return func_ret

    return wrapper
