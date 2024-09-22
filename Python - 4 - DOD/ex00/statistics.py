from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Print the result of the statistical function specified in the kwargs.

    Args:
        *args: The list of numbers.
        **kwargs: The statistical function to apply on the list of numbers
            (mean, median, quartile
            std, var).
    Returns:
        None.
    Logic:
        - Create a list of dictionaries containing the name of the statistical
        function and the function itself.
        - Iterate over the kwargs and check if the value is in the list of
        dictionaries.
        - If it is, call the function with the list of numbers and print the
        result.
        - If the value is not in the list of dictionaries, print "ERROR".
    """
    functions_dict = [
        {
            "name": "mean",
            "function": mean,
        },
        {
            "name": "median",
            "function": median,
        },
        {
            "name": "quartile",
            "function": quartile,
        },
        {
            "name": "std",
            "function": std,
        },
        {
            "name": "var",
            "function": var,
        }
    ]
    for key, value in kwargs.items():
        for function in functions_dict:
            if value == function["name"]:
                try:
                    return_val = function["function"](*args)
                    print(f"{value}: {return_val}")
                except AssertionError:
                    print("ERROR")
    return None


def mean(*args: Any) -> float:
    """
    Calculate the mean of a list of numbers.
    """
    if len(args) == 0:
        raise AssertionError
    return sum(args) / len(args)


def median(*args: Any) -> float:
    """
    Calculate the median of a list of numbers.
    """
    if len(args) == 0:
        raise AssertionError
    tmp = sorted(args)
    n = len(args)
    if n % 2 == 0:
        return (tmp[n // 2 - 1] + tmp[n // 2]) / 2
    else:
        return tmp[n // 2]


def quartile(*args: Any) -> float:
    """
    Calculate the quartile of a list of numbers.
    """
    if len(args) == 0:
        raise AssertionError
    tmp = sorted(args)
    n = len(tmp)
    q1 = tmp[n // 4]
    q3 = tmp[3 * n // 4]
    return q1, q3


def std(*args: Any) -> float:
    """
    Calculate the standard deviation of a list of numbers.
    """
    if len(args) == 0:
        raise AssertionError
    m = mean(*args)
    _sum = 0
    for x in args:
        _sum += (x - m) ** 2
    return (_sum / len(args)) ** 0.5


def var(*args: Any) -> float:
    """
    Calculate the variance of a list of numbers.
    """
    if len(args) == 0:
        raise AssertionError
    return std(*args) ** 2
