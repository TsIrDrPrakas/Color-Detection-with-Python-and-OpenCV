# working code
import numpy as np
import cv2

def get_limits(color):
    """
    Calculates lower and upper HSV limits for a given BGR color.

    Args:
        color: A tuple of BGR values (e.g., (0, 255, 255) for yellow).

    Returns:
        A tuple containing the lower and upper HSV limits as NumPy arrays.
    """

    c = np.uint8([[color]])  # Convert to NumPy array

    """
    # Dont RUN this
    # Handle grayscale images
    if len(c.shape) == 2:
        c = cv2.cvtColor(c, cv2.COLOR_GRAY2BGR)
    """

    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = hsvC[0][0][0]

    """
    # Dont RUN this
    lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
    upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    """

    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperlimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperlimit