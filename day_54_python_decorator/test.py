import time

current_time = time.time()


def speed_calc_decorator(function_to_test):

    function_name = function_to_test.__name__

    def wrapper_function():
        function_to_test()
        time_difference = time.time() - current_time
        print(f"The time taken for {function_name} is {time_difference}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
