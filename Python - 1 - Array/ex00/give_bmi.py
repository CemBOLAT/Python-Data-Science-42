import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    return_value = []
    try:
        if len(height) == 0 or len(weight) == 0:
            raise ValueError("Error - Empty list")
        if len(height) != len(weight):
            raise ValueError("Error - Different length")
        if 0 in height or float(0) in height:
            raise ValueError("Error - Zero height")
        if 0 in weight or float(0) in weight:
            raise ValueError("Error - Zero weight")
        for i in range(len(height)):
            if (type(height[i]) != int and type(height[i]) != float) or (type(weight[i]) != int and type(weight[i]) != float):
                raise ValueError("Error - Invalid type")
            bmi = weight[i] / np.square(height[i])
            return_value.append(bmi)
    except ValueError as e:
        print(e)
        return_value = None
    return return_value

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return_value = []
    for i in range(len(bmi)):
        return_value.append(bmi[i] > limit)
    return return_value