import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        if type(family) != list or type(start) != int or type(end) != int:
            raise ValueError("Error - Invalid type")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family[start:end]).shape}")
        return np.array(family[start:end]).tolist()
    except ValueError as e:
        print(e)
        return_value = None
    return return_value
