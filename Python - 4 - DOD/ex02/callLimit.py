from typing import Any

def callLimit(limit: int):
    """
    Decorator that limits the number of times a function can be called

    Args:
    limit: int - the maximum number of times the function can be called

    Returns:
    function - the decorated function
    """
    count = 0
    def callLimiter(function):
        """
        Wrapper function that limits the number of times the function can be called

        Args:
        function: function - the function to be decorated

        Returns:
        function - the decorated function
        """
        def limit_function(*args: Any, **kwds: Any):
            """
            Inner function that checks if the function has been called too many times

            Args:
            *args: Any - the arguments passed to the function
            **kwds: Any - the keyword arguments passed to the function
            
            Returns:
            Any - the result of the function call or None if the function has been called too many times
            """
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
                return None
        return limit_function
    return callLimiter