from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def save_zoom_and_grayscale_image(top, left, right, bottom, img):
    """
    This function saves the zoomed and grayscaled image.

    Args:
        top (int): The top coordinate.
        left (int): The left coordinate.
        right (int): The right coordinate.
        bottom (int): The bottom coordinate.
        img (Image): The image object.

    Returns:
        None

    Logic:
        - Crop the image using the given dimensions.
        - Save the cropped image.
        - Convert the cropped image to grayscale.
        - Save the grayscaled image.
    """
    zoomed_image = img.crop((left, top, right, bottom))
    zoomed_image.save("zoomed_image.jpeg")
    grayscaled_image = zoomed_image.convert("L")
    grayscaled_image.save("grayscaled_image.jpeg")


def transpose_image(array_image):
    """
    This function transposes the image.

    Args:
        array_image (np.ndarray): The image array.

    Returns:
        np.ndarray: The transposed image array.
    """
    return np.transpose(array_image)


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
        - Save the zoomed and grayscaled image.
        - Load the grayscaled image using ft_load.
        - Check if the return type is a numpy array.
        - Open the grayscaled image using PIL.
        - Transpose the image.
        - Display the transposed image.
    """
    top = 100
    bottom = 500
    left = 450
    right = 850
    try:
        with Image.open("animal.jpeg") as img:
            save_zoom_and_grayscale_image(top, left, right, bottom, img)
        grayscaled_image_array = ft_load("grayscaled_image.jpeg")
        if not isinstance(grayscaled_image_array, np.ndarray):
            raise AssertionError("Error - Invalid return type")
        with Image.open("grayscaled_image.jpeg") as img:
            print("The shape of image is: ", end="")
            print(f"({img.size[1]}, {img.size[0]}, {img.layers})")
            print(grayscaled_image_array)
            transposed_image = transpose_image(grayscaled_image_array)
            print(f"New shape after Transpose: {transposed_image.shape}")
            print(transposed_image)
            plt.imshow(transposed_image, cmap='gray')
            plt.title("Transposed Grayscaled Zoomed Image")
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
