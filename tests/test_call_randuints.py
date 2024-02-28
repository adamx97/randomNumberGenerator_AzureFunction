import unittest
import azure.functions as func
import json

# test by running python -m pytest tests (not pytest tests, as the docs say)

# from function_app import my_second_function
from function_app import randuints
from testUtils import TestUtils


class TestFunction(unittest.TestCase):
    # testing on this platform established that an uint is 4 bytes (32 bits)
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.testUtils = TestUtils()

    def test_randuints_0(self):
        # Construct a mock HTTP request.
        count = 0
        req = func.HttpRequest(
            method="GET",
            body=None,
            url="/api/randuints",
            params={"count": count},
        )
        # Call the function.
        func_call = randuints.build().get_user_function()
        resp = func_call(req)
        body = resp.get_body()
        body = body.decode("utf-8")  # cast bytes[] to string to ease the upcoming tests
        print(f"body is a {type(body)}")
        # Check the output.
        self.assertIn("Random number(s):", body)
        mys = (
            f"1 unsigned integer(s)"  # default is 1, we will not return 0 random ints.
        )
        self.assertIn(mys, body)
        result_start = body.find("Random number(s):<br />") + len(
            "Random number(s):<br />"
        )
        result_end = len(body)
        result = body[result_start:result_end]
        self.assertEqual(1, len(result.split(", ")))
        self.testUtils.TestRange(result.split(", "), 32)

    def test_randuints_10(self):
        # Construct a mock HTTP request.
        count = 10
        req = func.HttpRequest(
            method="GET",
            body=None,
            url="/api/randuints",
            params={"count": count},
        )
        # Call the function.
        func_call = randuints.build().get_user_function()
        resp = func_call(req)
        body = resp.get_body()
        body = body.decode("utf-8")  # cast bytes[] to string to ease the upcoming tests
        print(f"body is a {type(body)}")
        # Check the output.
        self.assertIn("Random number(s):", body)
        mys = f"{count} unsigned integer(s)"
        self.assertIn(mys, body)
        result_start = body.find("Random number(s):<br />") + len(
            "Random number(s):<br />"
        )
        result_end = len(body)
        result = body[result_start:result_end]
        self.assertEqual(count, len(result.split(", ")))
        self.testUtils.TestRange(result.split(", "), 32)

    def test_randuints_string(self):
        # Construct a mock HTTP request.
        count = 10
        req = func.HttpRequest(
            method="GET",
            body=None,
            url="/api/randuints",
            params={"count": count, "output": "string"},
        )
        # Call the function.
        func_call = randuints.build().get_user_function()
        resp = func_call(req)
        body = resp.get_body()
        body = body.decode("utf-8")  # cast bytes[] to string to ease the upcoming tests
        print(f"body is a {type(body)}")
        # Check the output.
        self.assertIn("Random number(s):", body)
        mys = f"{count} unsigned integer(s)"
        self.assertIn(mys, body)
        result_start = body.find("Random number(s):<br />") + len(
            "Random number(s):<br />"
        )
        result_end = len(body)
        result = body[result_start:result_end]
        self.assertEqual(count, len(result.split(", ")))
        self.testUtils.TestRange(result.split(", "), 32)

    def test_randuints_json(self):
        # Construct a mock HTTP request.
        count = 1000
        req = func.HttpRequest(
            method="GET",
            body=None,
            url="/api/randuints",
            params={"count": count, "output": "json"},
        )
        # Call the function.
        func_call = randuints.build().get_user_function()
        resp = func_call(req)
        body = resp.get_body()
        jsonbody = json.loads(body)
        print(f"jsonbody is a {type(jsonbody)}")

        self.assertEqual(count, len(jsonbody))
        self.testUtils.TestRange(jsonbody, 32)
