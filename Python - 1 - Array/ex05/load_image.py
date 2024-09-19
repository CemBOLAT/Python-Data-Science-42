import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.array:
    """
    Parameters
        path : str
            The path of the image
    Returns
        np.array
            The image as an array
    Raises
        ValueError
            If path is not a string or the file extension is not .jpg or .jpeg
        FileNotFoundError
            If the file is not found
        PermissionError
            If the file is not accessible
        Exception
            For any other exception
    Logic
        - Check if path is a string
        - Check if the file extension is .jpg or .jpeg
        - Check if the file exists
        - Open the image
        - Print the shape of the image
        - Return the image as an array
    """
    try:
        if not isinstance(path, str):
            raise ValueError("Error - Invalid type")
        if not path.endswith(".jpg") and not path.endswith(".jpeg"):
            raise ValueError("Error - Invalid file extension")
        if not os.path.exists(path):
            raise FileNotFoundError("Error - File not found")
        with Image.open(path) as img:
            print(f"The shape of image is: ({img.size[1]}, {img.size[0]}, {img.layers})")
            return np.array(img)
    except ValueError as e:
        print(e)
        return []
    except FileNotFoundError as e:
        print(e)
        return []
    except PermissionError as e:
        print(e)
        return []
    except Exception as e:
        print(e)
        return []
