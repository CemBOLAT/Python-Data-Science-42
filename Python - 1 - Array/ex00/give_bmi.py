def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """
    Parameters:
        height: list[int | float] -> list of heights
        weight: list[int | float] -> list of weights
    Returns:
        list[int | float]
    Description:
        This function takes a list of heights and a list of\
            weights as arguments.
        It calculates the BMI of each person and returns a list of BMIs.
    Raises:
        AssertionError: If the length of height and weight is different
        AssertionError: If the type of height or weight is not int or float
        AssertionError: If the value of height or weight is\
            less than or equal to 0
    """
    return_value = []
    try:
        if len(height) != len(weight):
            raise \
                AssertionError("Error - Different length of height and weight")
        for i in range(len(height)):
            if (not isinstance(height[i], (int, float))) \
                    or (not isinstance(weight[i], (int, float))):
                raise \
                    AssertionError("Error - Invalid type in height or weight")
            if height[i] <= 0 or weight[i] <= 0:
                raise \
                    AssertionError("Error - Invalid value in height or weight")
            bmi = weight[i] / (height[i] ** 2)
            return_value.append(bmi)
        return return_value
    except AssertionError as e:
        print(e)
    return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Parameters:
        bmi: list[int | float] -> list of BMIs
        limit: int -> limit value
    Returns:
        list[bool]
    Description:
        This function takes a list of BMIs and a limit value as arguments.
        It returns a list of boolean values where True \
            indicates that the BMI is greater than the limit value.
    Raises:
        AssertionError: If the type of limit is not int
        AssertionError: If the value of limit is less than or equal to 0
        AssertionError: If the type of bmi is not int or float
    """
    return_value = []
    try:
        if not isinstance(limit, int):
            raise AssertionError("Error - Invalid type in limit")
        if limit <= 0:
            raise AssertionError("Error - Invalid limit value")
        if not all(isinstance(i, (int, float)) for i in bmi):
            raise AssertionError("Error - Invalid type in bmi")

        for i in range(len(bmi)):
            return_value.append(bmi[i] > limit)
        return return_value
    except AssertionError as e:
        print(e)
    return []
