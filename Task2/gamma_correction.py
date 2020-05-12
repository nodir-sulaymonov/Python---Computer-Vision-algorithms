from __future__ import print_function
from sys import argv
import os.path
import cv2
import numpy as np
import matplotlib.pyplot as ptl

def gamma_correction(src_path, dst_path, a, b):
    image = cv2.imread(src_path)
    img_change = image.astype(np.float64)
    image_formul = a * (img_change ** b)
    out_array = np.clip(image_formul, a_min=0, a_max=255)
    out_array = out_array.astype(np.uint8)
    cv2.imwrite(dst_path, out_array)

gamma_correction('12.jpg', 'name.jpg', 1, 1.8)
if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])
    argv[3] = float(argv[3])
    argv[4] = float(argv[4])

    gamma_correction(*argv[1:])
