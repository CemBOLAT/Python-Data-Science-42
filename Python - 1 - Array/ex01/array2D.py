import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Parameters
        family : list
            A list of lists
        start : int
            The starting index
        end : int
            The ending index
    Returns
        list
            A list of lists
    Raises
        AssertionError
            If family is not a list of lists, \
                start is not an integer, end is not an integer, \
                family is empty, or the inner lists are not of the same length
    Logic
        - Check if family is a list of lists
        - Check if start and end are integers
        - Check if family is not empty
        - Check if inner lists are of the same length
        - Print the shape of the input list
        - Print the shape of the sliced list
        - Return the sliced list
    """
    try:
        if (not isinstance(family, list)) \
                or (not isinstance(start, int)) or (not isinstance(end, int)):
            raise AssertionError("Error - Invalid function parameters")
        if (len(family) == 0):
            raise AssertionError("Error - Empty list")
        for innerList in family:
            if not isinstance(innerList, list):
                raise AssertionError("Error - Invalid type in family")
            if len(innerList) != len(family[0]):
                raise AssertionError("Error - Different length of inner lists")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family[start:end]).shape}")
        return np.array(family[start:end]).tolist()
    except AssertionError as e:
        print(e)
    return []
