def square(x: int | float) -> int | float:
    """
    Return the square of a number.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Return the power of a number.
    """
    return x ** x

def outer(x: int | float, function) -> object:
    """
    Parameters
    ----------
    x : int | float
        The input number.
    function : function
        The function to apply to the input number.
    
    Returns
    -------
    object
        The output of the function applied to the input number.
    """
    count = 0
    def inner():
        """
        Apply the function to the input number.

        Returns
        -------
        object
            The output of the function applied to the input number.
        
        """
        nonlocal count
        count += 1

        nonlocal x
        x = function(x)
        return x
    return inner