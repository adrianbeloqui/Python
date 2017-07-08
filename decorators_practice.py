"""Module to test basic functionality of decorators
"""

import time


def log(func):
    """Simple decorator
    """
    def wrap():
        """Wrapper function that logs time that took to run the function
        """
        start = time.time()
        result = func()
        print("Run time - {0} seconds".format(time.time() - start))
        return result
    return wrap


@log
def sum_nums():
    """Simple function that consumes log decorator
    """
    return 2 + 2


def log_user(func):
    """Simple decorator for a function with one argument
    """
    def wrap(user):
        """Wrapper function that logs the user that is logged in
        """
        print("## User - {0} ##".format(user))
        return func(user)
    return wrap


@log_user
def login(user):
    """Simple function that requires one argument
    """
    return user + " logged."


def decor_with_args(*args, **kwargs):
    """Simple decorator that receives arguments
    """
    def decor(func):
        """Inner wrapper that receives the function from the decorator with args
        """
        def wrap():
            """Wrapper function that logs the arguments that the decorator receives
            """
            print("Arguments " + str(args))
            print("Keywords args: " + str(kwargs))
            return func()
        return wrap
    return decor


@decor_with_args(hola='arg1', user="Adrian")
def test():
    """Simple function that uses a decorator with arguments
    """
    return "Worked!"
