from timeit import timeit
from rd_functions import call_rdrand16_retry
import ctypes


def add_test_set(iterable):
    for i in range(10000):
        iterable.add(i)


def add_test_list(iterable):
    for i in range(10000):
        iterable.append(i)


def add_test_array(iterable):
    for i in range(10000):
        iterable.append(i)


execution_time = timeit(
    "add_test_set(iterable)",
    setup="from __main__ import add_test_set; iterable = set()",
    number=1000,
)
print(f"SET Execution time: {execution_time} seconds")

execution_time = timeit(
    "add_test_list(iterable)",
    setup="from __main__ import add_test_list; iterable = list()",
    number=1000,
)
print(f"LIST Execution time: {execution_time} seconds")


execution_time = timeit(
    "add_test_array(iterable)",
    setup="from __main__ import add_test_array; my_array = []; iterable = my_array",
    number=1000,
)
print(f"ARRAY Execution time: {execution_time} seconds")

# my_array = []
# add_test_array(my_array)

print(call_rdrand16_retry(10))
