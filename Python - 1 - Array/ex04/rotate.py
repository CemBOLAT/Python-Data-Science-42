from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os

def save_zoom_and_grayscale_image(top, left, right, bottom, img):
    zoomed_image = img.crop((left, top, right, bottom))
    zoomed_image.save("zoomed_image.jpeg")
    grayscaled_image = zoomed_image.convert("L")
    grayscaled_image.save("grayscaled_image.jpeg")

def transpose_image(array_image):
    return np.transpose(array_image)

def main():
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
            print(F"The shape of image is: ({img.size[1]}, {img.size[0]}, {img.layers})")
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
    except KeyboardInterrupt as e:
        pass
if __name__ == "__main__":
    main()