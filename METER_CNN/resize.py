import numpy as np 
import matplotlib.pyplot as plt
import os
import cv2
import random 
import pickle

DATADIR = "dataset/"
IMG_SIZE = 28
CATEGORIES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# cv2.resize(image,(width,height))
def resize():
    for categories in CATEGORIES:
        path = os.path.join(DATADIR, categories)
        print(path)
        for img in os.listdir(path):
            img_arr = cv2.imread(os.path.join(path, img))
            print(img)
            img_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))
            plt.imshow(img_arr)
            plt.show()
            imwrite(path)
            break
        break