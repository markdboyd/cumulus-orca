"""
This module contains helper functions for the unit tests.
"""
import json



def create_handler_event():
    try:
        with open('test/testevents/fixture1.json') as f:
            event = json.load(f)
    except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
        with open('testevents/fixture1.json') as f:
            event = json.load(f)
    return event


class LambdaContextMock:
    def __init__(self):
        self.function_name = "request_files"
        self.function_version = 1
        self.invoked_function_arn = "arn:aws:lambda:us-west-2:065089468788:function:request_files:1"
