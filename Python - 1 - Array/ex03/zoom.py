from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os


def main():

    try:
        array_image = ft_load("animal.jpeg")
        if not isinstance(array_image, np.ndarray):
            raise AssertionError("Error - Invalid return type")
        with Image.open("animal.jpeg") as img:
            img.show()
    except AssertionError as e:
        print("AssertionError: ", e)
    except FileNotFoundError as e:
        print("FileNotFoundError: ", e)
    except PermissionError as e:
        print("PermissionError: ", e)

if __name__ == "__main__":
    main()