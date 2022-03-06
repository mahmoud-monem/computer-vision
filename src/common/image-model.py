import cv2 as cv
import numpy as np


class ImageModel:
    image_gray: np.ndarray
    image_rgb: np.ndarray

    def __init__(self, path: str):
        self.image_rgb = cv.imread('assets/images/spartacus.jpg')
        self.image_gray = self.rgb2gray(self.image_rgb)
        pass

    @staticmethod
    def rgba2rgb(rgba):
        return rgba[:, :, :-1]

    @staticmethod
    def rgb2gray(img: np.ndarray) -> np.ndarray:
        ret: np.ndarray
        if (img.ndim == 2):
            ret = img
        elif img.shape[-1] == 4:
            print("rgba image to gray")
            img = ImageModel.rgba2rgb(img)
            ret = np.dot(img[..., :3], [0.299, 0.587, 0.114])
        else:
            ret = np.dot(img[..., :3], [0.299, 0.587, 0.114])
        return ret


if __name__ == '__main__':
    img = ImageModel()
