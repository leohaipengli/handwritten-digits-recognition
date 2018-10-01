import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image
from binascii import a2b_base64
import io

def dataurl_to_pil(data):
    """
    given a dataURL, convert it to PIL.Image object
    :param data: the base64 part saved
    :return: PIL.Image
    """
    temp_filename = 'temp_img.png'
    binary_data = a2b_base64(data)

    return Image.open(io.BytesIO(binary_data))