import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array):
    """
    Inverts the colors of the input image.

    Parameters
    ----------
    array : np.array
        The image as a NumPy array with shape (height, width, channels).

    Returns
    -------
    None

    Logic
    -----
    - A new image array is created with \
        the same dimensions as the input but filled with zeros.
    - The colors in each channel (Red, Green, Blue) \
        are subtracted from 255 to invert the colors.
    - The resulting inverted image is displayed using matplotlib.
    """
    image = np.zeros_like(array)
    image[:, :, 0] = 255 - array[:, :, 0]
    image[:, :, 1] = 255 - array[:, :, 1]
    image[:, :, 2] = 255 - array[:, :, 2]

    plt.title("Inverted Image")
    plt.imshow(image)
    plt.show()


def ft_red(array):
    """
    Displays only the red channel of the input image.

    Parameters
    ----------
    array : np.array
        The image as a NumPy array with shape (height, width, channels).

    Returns
    -------
    None

    Logic
    -----
    - A new image array is created \
        with the same dimensions as the input but filled with zeros.
    - The red channel of the input \
        image is copied to the red channel of the new image.
    - The new image with only the \
        red channel is displayed using matplotlib.
    """
    reds = array[:, :, 0]
    image = np.zeros_like(array)
    image[:, :, 0] = reds

    plt.title("Red Image")
    plt.imshow(image)
    plt.show()


def ft_green(array):
    """
    Displays only the green channel of the input image.

    Parameters
    ----------
    array : np.array
        The image as a NumPy array with shape (height, width, channels).

    Returns
    -------
    None

    Logic
    -----
    - A new image array is created \
        with the same dimensions as the input but filled with zeros.
    - The green channel of the input \
        image is copied to the green channel of the new image.
    - The new image with only the green \
        channel is displayed using matplotlib.
    """
    greens = array[:, :, 1]
    image = np.zeros_like(array)
    image[:, :, 1] = greens

    plt.title("Green Image")
    plt.imshow(image)
    plt.show()


def ft_blue(array):
    """
    Displays only the blue channel of the input image.

    Parameters
    ----------
    array : np.array
        The image as a NumPy array with shape (height, width, channels).

    Returns
    -------
    None

    Logic
    -----
    - A new image array is created with \
        the same dimensions as the input but filled with zeros.
    - The blue channel of the input image \
        is copied to the blue channel of the new image.
    - The new image with only the blue \
        channel is displayed using matplotlib.
    """
    blues = array[:, :, 2]
    image = np.zeros_like(array)
    image[:, :, 2] = blues

    plt.title("Blue Image")
    plt.imshow(image)
    plt.show()


def ft_grey(array):
    """
    Converts the input image to grayscale \
        using the average of the RGB channels.

    Parameters
    ----------
    array : np.array
        The image as a NumPy array with shape (height, width, channels).

    Returns
    -------
    None

    Logic
    -----
    - The red, green, and blue channels of the input image are averaged.
    - The resulting grayscale values are applied \
        to all three channels (R, G, B) to create a grayscale image.
    - The grayscale image is displayed using matplotlib.
    """
    reds = array[:, :, 0]
    greens = array[:, :, 1]
    blues = array[:, :, 2]
    greys = (reds / 3) + (greens / 3) + (blues / 3)
    image = np.zeros_like(array)
    image[:, :, 0] = greys
    image[:, :, 1] = greys
    image[:, :, 2] = greys

    plt.title("Grey Image")
    plt.imshow(image)
    plt.show()
