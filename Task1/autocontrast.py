from __future__ import print_function
from sys import argv
import os.path
import cv2
import numpy as np
import matplotlib.pyplot as plt



def autocontrast(src_path, dst_path, white_perc, black_perc):
    image = cv2.imread(src_path)
    img_change = image.astype(np.float64)
    black_persent = np.percentile(img_change, black_perc * 100)
    white_persent = np.percentile(img_change, 100 - white_perc * 100)
    img_change = (img_change - black_persent) / (white_persent - black_persent) * 255
    img_change[img_change > 255] = 255
    img_change[img_change < 0] = 0
    img_change = img_change.astype(np.uint8)
    cv2.imwrite(dst_path, img_change)

autocontrast('12.jpg', 'change.jpg', 0.1, 0.2)

if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])
    argv[3] = float(argv[3])
    argv[4] = float(argv[4])

    assert 0 <= argv[3] < 1
    assert 0 <= argv[4] < 1

    autocontrast(*argv[1:])
