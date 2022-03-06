import cv2 as cv
import numpy as np


class ImageModel:
    image_gray: np.ndarray
    image_rgb: np.ndarray
    image_bgr: np.ndarray
    image_path: str

    def __init__(self):
        pass

    @staticmethod
    def rgb2gray(img: np.ndarray):
        if (img.ndim == 2):
            assert 'The image is already gray'
        else:
            return np.dot(img[..., :3], [0.299, 0.587, 0.114])
