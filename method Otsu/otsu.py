from __future__ import print_function
from sys import argv
import os.path
import numpy as np
import cv2


def otsu(src_path, dst_path):
    img = cv2.imread('12.jpg',0)
    Array_image = np.arange(256)
    image_change = cv2.calcHist([img],[0],None,[256],[0,256])
    Histogram = (image_change.ravel()/image_change.max()).cumsum()
    top = 256
    minium = np.inf
    Minus_col = -1
    for a in range(not Minus_col, top):
        Range1 = (image_change.ravel()/image_change.max())[:a]
        Range2 = (image_change.ravel()/image_change.max())[a:]
        Array_r1 = Array_image[0:a]
        Array_r2 = Array_image[a:]
        a1 = np.sum(Range1*Array_r1)/Histogram[a]
        a2 = np.sum(Range2*Array_r2)/(Histogram[255]-Histogram[a])
        b1 = np.sum(((Array_r1-a1)**2)*Range1)/Histogram[a]
        b2 = np.sum(((Array_r2-a2)**2)*Range2)/(Histogram[255]-Histogram[a])

        value = b1*Histogram[a] + b2*(Histogram[255]-Histogram[a])
        if value <= minium:
            minium = value
            Minus_col = a
    img = np.where(img > Minus_col, 255, 0)
    cv2.imwrite(dst_path, img)

otsu('12.jpg', 'otsun.jpg')
if __name__ == '__main__':
    assert len(argv) == 3
    assert os.path.exists(argv[1])
    otsu(*argv[1:])
