import time
current = time.time()
print(current)

def speed_calc_decorator(function):
    def wraper_function():        
        start = time.time()
        function()
        end = time.time()
        duration = end - start
        return duration
    return wraper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i

print(fast_function())
print(slow_function())