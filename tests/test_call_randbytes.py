import unittest
import azure.functions as func
import json

# test by running python -m pytest tests (not pytest tests, as the docs say)

# from function_app import my_second_function
from function_app import randbytes
from testUtils import TestUtils


class TestFunction(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.testUtils = TestUtils()

    def test_randbytes_0(self):
        # Construct a mock HTTP request.
        count = 0
        req = func.HttpRequest(
            method="GET",
            body=None,
            url="/api/randbytes",
            params={"count": count},
        )
        # Call the function.
        func_call = randbytes.build().get_user_function()
        resp = func_call(req)
        body = resp.get_body()
        body = body.decode("utf-8")  # cast bytes[] to string to ease the upcoming tests
        print(f"body is a {type(body)}")
        # Check the output.
        self.assertIn("Byte(s):", body)
        mys = f"1 byte(s)"  # default is 1, we will not return 0 random ints.
        self.assertIn(mys, body)
        result_start = body.find("Byte(s):<br />") + len("Byte(s):<br />")
        result_end = len(body)
        result = body[result_start:result_end]
        self.assertEqual(2, len(result))  # it should be 2 chars long.
        vals = list(map(lambda x: str(int(x, 16)), result.split(" ")))
        self.testUtils.TestRange(vals, 8)

    def test_randbytes_10(self):
        # Construct a mock HTTP request.
        count = 10
        req = func.HttpRequest(
            method="GET",
            body=None,
            url="/api/randbytes",
            params={"count": count},
        )
        # Call the function.
        func_call = randbytes.build().get_user_function()
        resp = func_call(req)
        body = resp.get_body()
        body = body.decode("utf-8")  # cast bytes[] to string to ease the upcoming tests
        print(f"body is a {type(body)}")
        # Check the output.
        self.assertIn("Byte(s):", body)
        mys = f"{count} byte(s)"
        self.assertIn(mys, body)
        result_start = body.find("Byte(s):<br />") + len("Byte(s):<br />")
        result_end = len(body)
        result = body[result_start:result_end]
        self.assertEqual(count, len(result.split(" ")))
        self.assertEqual((count * 3) - 1, len(result))
        vals = list(map(lambda x: str(int(x, 16)), result.split(" ")))
        self.testUtils.TestRange(vals, 8)

    def test_randbytes_string(self):
        # Construct a mock HTTP request.
        count = 10
        req = func.HttpRequest(
            method="GET",
            body=None,
            url="/api/randbytes",
            params={"count": count, "output": "string"},
        )
        # Call the function.
        func_call = randbytes.build().get_user_function()
        resp = func_call(req)
        body = resp.get_body()
        body = body.decode("utf-8")  # cast bytes[] to string to ease the upcoming tests
        print(f"body is a {type(body)}")
        # Check the output.
        self.assertIn("Byte(s):", body)
        mys = f"{count} byte(s)"
        self.assertIn(mys, body)
        result_start = body.find("Byte(s):<br />") + len("Byte(s):<br />")
        result_end = len(body)
        result = body[result_start:result_end]
        self.assertEqual(count, len(result.split(" ")))
        self.assertEqual((count * 3) - 1, len(result))
        vals = list(map(lambda x: str(int(x, 16)), result.split(" ")))
        self.testUtils.TestRange(vals, 8)

    def test_randbytes_json(self):
        # Construct a mock HTTP request.
        count = 1000
        req = func.HttpRequest(
            method="GET",
            body=None,
            url="/api/randbytes",
            params={"count": count, "output": "json"},
        )
        # Call the function.
        func_call = randbytes.build().get_user_function()
        resp = func_call(req)
        body = resp.get_body()
        jsonbody = json.loads(body)
        print(f"jsonbody is a {type(jsonbody)}")
        self.assertEqual(count, len(jsonbody))
        vals = list(map(lambda x: str(int(x, 16)), jsonbody))
        self.testUtils.TestRange(vals, 8)
