from __future__ import print_function
from sys import argv
import os.path
import numpy as np
import cv2


def box_flter(src_path, dst_path, w, h):
    image = cv2.imread(src_path)
    img_change = image.astype(np.float64)
    a = np.cumsum(img_change, axis=0)
    I = np.cumsum(a, axis=1)
    A = I[0:-h, 0:-w]
    B = I[h:, w:]
    C = I[0:-h, w:]
    D = I[h:, 0:w]
    L = (C + A) - (B + D) / w * h
    img_out = L.astype(np.uint8)
    cv2.imwrite(dst_path, img_out)

    box_flter('12.jpg', 'second.jpg', 1, 1)


if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])
    argv[3] = int(argv[3])
    argv[4] = int(argv[4])
    assert argv[3] > 0
    assert argv[4] > 0

    box_flter(*argv[1:])
