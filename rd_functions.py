import ctypes
import platform
from timeit import timeit
import struct
import rd_functions_p


rdObj = rd_functions_p.RdFunctions()


def add_test_set(iterable):
    for i in range(10000):
        n = rdObj.RdRand16_Retry(10)
        iterable.add(n)


def add_test_list(iterable):
    for i in range(10000):
        n = rdObj.RdRand16_Retry(10)
        iterable.append(n)


def add_test_array(iterable):
    for i in range(10000):
        n = rdObj.RdRand16_Retry(10)
        iterable.append(n)


def add_test_tuple_uints():
    n = rdObj.RdRand_Get_N_Uints(10000)
    x = tuple(n)
    # return x
    # print("Tuple contents (first 10): {0} Length: {1}").format(x[:10], len(x))


def add_test_tuple_bytes():
    n = rdObj.RdRand_Get_Bytes(10000)
    x = tuple(n)
    z = 1 + 2
    # return x
    # print("Tuple contents (first 10): {0} Length: {1}").format(x[:10], len(x))


def speedtest():
    print("Starting Speedtest")
    # Tuple works the best as it doesn't try to determine membership when inserting the values
    # Results when set to 100 iterations (* 10000 method calls/objects per iteration)= 1M calls/objects.
    # SET Execution time: 5.965435177000472 seconds
    # LIST Execution time: 5.396032759999798 seconds
    # ARRAY Execution time: 6.417413571001816 seconds
    # MULTIPLE Uints into a tuple Execution time: 1.0632295120012714 seconds
    # MULTIPLE Bytes into a tuple Execution time: 0.2005292020003253 seconds
    # Results when set to 1000 iterations * 10000 method calls/objects per iteration = 10M calls/objects.
    # SET Execution time: 71.01541434499813 seconds
    # LIST Execution time: 55.00359590299922 seconds
    # ARRAY Execution time: 57.14912452899807 seconds
    # MULTIPLE Uints into a tuple Execution time: 11.938809104998654 seconds
    # MULTIPLE Bytes into a tuple Execution time: 4.00682676499855 seconds
    mynumber = 10

    execution_time = timeit(
        "add_test_set(iterable)",
        setup="from __main__ import add_test_set; iterable = set()",
        number=mynumber,
    )
    print(f"SET Execution time: {execution_time} seconds")

    execution_time = timeit(
        "add_test_list(iterable)",
        setup="from __main__ import add_test_list; iterable = list()",
        number=mynumber,
    )
    print(f"LIST Execution time: {execution_time} seconds")

    execution_time = timeit(
        "add_test_array(iterable)",
        setup="from __main__ import add_test_array; my_array = []; iterable = my_array",
        number=mynumber,
    )
    print(f"ARRAY Execution time: {execution_time} seconds")
    execution_time = timeit(
        "add_test_tuple_uints()",
        setup="from __main__ import add_test_tuple_uints;",
        number=mynumber,
    )
    print(f"MULTIPLE Uints into a tuple Execution time: {execution_time} seconds")

    execution_time = timeit(
        "add_test_tuple_bytes()",
        setup="from __main__ import add_test_tuple_bytes;",
        number=mynumber,
    )
    print(f"MULTIPLE Bytes into a tuple Execution time: {execution_time} seconds")


# Call the functions
def checktuples():
    print("Checking ints tuple output")
    for i in range(0, 1000, 100):
        print("Iteration: {0}".format(i))
        n = rdObj.RdRand_Get_N_Uints(i)
        print("Uint contents (first 10): {0} Length: {1}".format(n[:10], len(n)))
        nt = tuple(n)
        print(
            "Uint tuple contents (first 10): {0} Length: {1}".format(nt[:10], len(nt))
        )
    print("Checking bytes tuple output")
    for i in range(0, 1000, 100):
        print("Iteration: {0}".format(i))
        b = rdObj.RdRand_Get_Bytes(i)
        print(r"Byte Length: {0}".format(len(b)))
        print(r"Byte contents (first 10): {0} ".format(b[:10]))
        bt = tuple(b)
        print(r"Byte tuple Length: {0}".format(len(bt)))
        print(
            r"Byte tuple contents (first 10): {0} Length: {1}".format(bt[:10], len(bt))
        )


n = rdObj.RdRand16_Retry(3)
print("Faster 16 bit: {0}".format(n))
print("Faster 32bit: {0}".format(rdObj.RdRand32_Retry(3)))
print("Faster 64bit: {0}".format(rdObj.RdRand64_Retry(3)))
n2 = rdObj.RdRand_Get_N_Uints(10)
print("10 uints: Uints are in a {0}".format(type(n2)))
for idx, nItem in enumerate(n2):
    print("{0}: {1}".format(idx, nItem))
t = ctypes.c_uint
print("On this platform, 1 uint is {0} bytes".format(ctypes.sizeof(ctypes.c_uint)))
print("Faster 10 uints: {0}".format(", ".join(map(str, n2))))
zz = rdObj.RdRand_Get_Bytes(10)
# print("Faster get bytes: {0}".format(struct.unpack(">h", zz)))
hexz = [hex(x) for x in zz]
intz = [x for x in zz]
print("Faster get bytes: {0}. As hex: {1}".format(intz, " ".join(hexz)))
checktuples()


speedtest()

# byte_array = bytes([65, 66, 67, 68])
# print(byte_array)
# int_value = int.from_bytes(byte_array, byteorder='big')
# print(int_value)
