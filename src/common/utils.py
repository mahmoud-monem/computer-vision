import numpy as np


class ImageUtile:

    @staticmethod
    def normalize(img: np.ndarray, new_min: int = 0, new_max: int = 255) -> np.ndarray:
        """
        normalization [summary]

        Parameters
        ----------
        img : np.ndarray
            [description]
        new_min : int, optional
            [description], by default 0
        new_max : int, optional
            [description], by default 255

        Returns
        -------
        np.ndarray
            [description]
        """
        old_min, old_max = img.min(), img.max()
        return (img - old_min) * (new_max - new_min) / (old_max - old_min) + new_min
