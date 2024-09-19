import numpy as np
from PIL import Image
import os

def ft_load(path: str) -> list:

    try:
        if type(path) != str:
            raise ValueError("Error - Invalid type")
        if path.endswith(".jpg") == False and path.endswith(".png") == False:
            raise ValueError("Error - Invalid file extension")
        if not os.path.exists(path):
            raise FileNotFoundError("Error - File not found")
        img = Image.open(path)
        print(
            f"The shape of Image is: {img.size[1]},{img.size[0]}, {img.layers}"
            )
        return np.array(img).tolist()
    except ValueError as e:
        print(e)
        return []
    except FileNotFoundError as e:
        print(e)
        return []
    except Exception as e:
        print(e)
        return []
