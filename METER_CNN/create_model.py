import numpy as np 
import matplotlib.pyplot as plt
import os
import cv2
import random 
import pickle

DATADIR = "dataset/"
IMG_SIZE = 25
CATEGORIES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
training_data = []
x, y = [], []


def creat_model():
    for categories in CATEGORIES:
        path = os.path.join(DATADIR, categories)
        print(path)
        for img in os.listdir(path):
            img_arr = cv2.imread(os.path.join(path, img))
            print(img)
            img_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))
            plt.imshow(img_arr)
            plt.show()
            break
        break


def create_training_data():
    for categories in CATEGORIES:
        path = os.path.join(DATADIR, categories)
        class_num = CATEGORIES.index(categories)
        for img in os.listdir(path):
            try:
                img_arr = cv2.imread(os.path.join(path, img))
                new_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_arr, class_num])
            except Exception as e:
                pass

if __name__ == "__main__":
    creat_model()
    random.shuffle(training_data)
    for features, label in training_data:
        x.append(features)
        y.append(label)
    print(len(x), len(y))
    pickle_out = open("x_t.pickle", "wb")
    pickle.dump(x, pickle_out)
    pickle_out.close()

    pickle_out = open("y_t.pickle", "wb")
    pickle.dump(y, pickle_out)
    pickle_out.close()

    