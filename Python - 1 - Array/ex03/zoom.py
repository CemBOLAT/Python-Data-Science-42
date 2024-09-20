from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def main():
    """
    This function reads an image, crops, grayscales, and displays it.

    Returns:
        None

    Raises:
        AssertionError: If the return type of ft_load is not a numpy array.
        FileNotFoundError: If the file is not found.
        PermissionError: If the user does not have the required permission.
        KeyboardInterrupt: If the user interrupts the program.

    Logic:
        - Load the image using ft_load.
        - Check if the return type is a numpy array.
        - Open the image using PIL.
        - Crop the image using the given dimensions.
        - Save the cropped image.
        - Convert the cropped image to grayscale.
        - Save the grayscaled image.
        - Load the grayscaled image using ft_load.
        - Check if the return type is a numpy array.
        - Open the grayscaled image using PIL.
        - Display the grayscaled image.
    """
    top = 100
    bottom = 500
    left = 450
    right = 850
    try:
        array_image = ft_load("animal.jpeg")
        if not isinstance(array_image, np.ndarray):
            raise AssertionError("Error - Invalid return type")
        with Image.open("animal.jpeg") as img:
            print("The shape of image is: ", end="")
            print(f"({img.size[1]}, {img.size[0]}, {img.layers})")
            print(array_image)
            z_image = img.crop((left, top, right, bottom))
            z_image.save("zoomed_image.jpeg")
        # L: grayscale - 1: binary - RGB: 3 - RGBA: 4 - CMYK: 4...
        grayscaled_image = z_image.convert("L")
        grayscaled_image.save("grayscaled_image.jpeg")
        grayscaled_image_array = ft_load("grayscaled_image.jpeg")
        if not isinstance(grayscaled_image_array, np.ndarray):
            raise AssertionError("Error - Invalid return type")
        with Image.open("grayscaled_image.jpeg") as img:
            print("New shape after slicing: ", end="")
            print(f"({img.size[1]}, {img.size[0]}, {img.layers})")
            print(grayscaled_image_array)
            plt.imshow(grayscaled_image_array, cmap='gray')
            plt.title("Grayscaled Zoomed Image")
            plt.show()
    except AssertionError as e:
        print("AssertionError: ", e)
    except FileNotFoundError as e:
        print("FileNotFoundError: ", e)
    except PermissionError as e:
        print("PermissionError: ", e)
    except KeyboardInterrupt:
        print("User Interruption")


if __name__ == "__main__":
    main()
