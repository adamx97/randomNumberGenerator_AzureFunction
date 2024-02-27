# <project_root>/rd_functions_p.py used to call dll from Python.  Named _p to avoid name collision with rd_functions.py
import ctypes
import platform
from timeit import timeit
import struct


class objRandomLib(object):
    _rd_functions_lib = None

    def __new__(self):
        if self._rd_functions_lib is None:
            self._rd_functions_lib = super(objRandomLib, self).__new__(self)
            # Check the operating system
            if platform.system() == "Linux":
                # Code to execute on Linux
                self._rd_functions_lib = ctypes.CDLL("./rd_functions.so")
                print("Running on Linux")
            elif platform.system() == "Windows":
                # Code to execute on Windows
                self._rd_functions_lib = ctypes.CDLL("./rd_functions.dll")
                print("Running on Windows")
            else:
                # Code to execute on other operating systems
                print("Running on unsupported OS: " + platform.system())
                raise ("Running on unsupported OS: " + platform.system())

            # Define the argument and return types for the functions
            self._rd_functions_lib.rdrand16_retry.argtypes = [
                ctypes.c_uint,
                ctypes.POINTER(ctypes.c_uint16),
            ]
            self._rd_functions_lib.rdrand16_retry.restype = ctypes.c_int

            self._rd_functions_lib.rdrand32_retry.argtypes = [
                ctypes.c_uint,
                ctypes.POINTER(ctypes.c_uint32),
            ]
            self._rd_functions_lib.rdrand32_retry.restype = ctypes.c_int

            self._rd_functions_lib.rdrand64_retry.argtypes = [
                ctypes.c_uint,
                ctypes.POINTER(ctypes.c_uint64),
            ]
            self._rd_functions_lib.rdrand64_retry.restype = ctypes.c_int

            self._rd_functions_lib.rdrand_get_n_uints.argtypes = [
                ctypes.c_uint,
                ctypes.POINTER(ctypes.c_uint),
            ]
            self._rd_functions_lib.rdrand_get_n_uints.restype = ctypes.c_int

            self._rd_functions_lib.rdrand_get_bytes.argtypes = [
                ctypes.c_uint,
                ctypes.POINTER(ctypes.c_ubyte),
            ]
            self._rd_functions_lib.rdrand_get_bytes.restype = ctypes.c_int
        return self._rd_functions_lib


class RdFunctions(object):
    def __init__(self):
        self._rd_functions_lib = objRandomLib()

    def RdRand16_Retry(self, retries=10):
        rand_num = ctypes.c_uint16()
        success = self._rd_functions_lib.rdrand16_retry(retries, ctypes.byref(rand_num))
        if success:
            # print("16 bit Random number generated:", rand_num.value)
            return rand_num.value
        else:
            raise ("16bit Error generating random number")

    def RdRand32_Retry(self, retries=10):
        rand_num = ctypes.c_uint32()
        success = self._rd_functions_lib.rdrand32_retry(retries, ctypes.byref(rand_num))
        if success:
            # print("32 bit Random number generated:", rand_num.value)
            return rand_num.value
        else:
            raise ("32 bit Error generating random number")

    def RdRand64_Retry(self, retries=10):
        rand_num = ctypes.c_uint64()
        success = self._rd_functions_lib.rdrand64_retry(retries, ctypes.byref(rand_num))
        if success:
            # print("64 bit Random number generated:", rand_num.value)
            return rand_num.value
        else:
            raise ("64 bit Error generating random number")

    def RdRand_Get_N_Uints(self, length):
        dest = (ctypes.c_uint * length)()  # Create an array of unsigned ints
        result = self._rd_functions_lib.rdrand_get_n_uints(length, dest)
        if result == length:
            return dest
            # print("Generated all requested random ints")
            # return ",".join(map(str, dest))
        else:
            raise ("Failed to generate all requested random ints. ")

    def RdRand_Get_Bytes(self, length):
        dest = (ctypes.c_ubyte * length)()  # Create an array of bytes
        result = self._rd_functions_lib.rdrand_get_bytes(length, dest)
        obytes = bytes(dest)
        if result == length:
            # print("Generated all requested random bytes")
            return obytes
        else:
            raise ("Failed to generate all requested random bytes")
