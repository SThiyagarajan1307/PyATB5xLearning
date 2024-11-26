import time


def time_decorator(func):
    def wrapper1():
        start_time = time.time()
        print("Start Time:", start_time)
        func()
        end_time = time.time()
        print("End Time:", end_time)
        print("Total Time Taken by Func ->", end_time - start_time)
    return wrapper1


def print_logs(func):
    def wrapper():
        print("Starting log")
        func()
        print("Ending log")
    return wrapper


@time_decorator
@print_logs
def test_ui_1():
    print("Executing test_ui_1")
    time.sleep(2)


@time_decorator
def test_ui_2():
    print("Executing test_ui_2")
    time.sleep(5)


#Run the functions to see results
test_ui_1()
test_ui_2()