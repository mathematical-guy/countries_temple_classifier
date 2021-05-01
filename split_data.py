import os
from sklearn.model_selection import train_test_split
from PIL import Image
import cv2
data = os.getcwd() + '/all_data/'

# total number of images
# print(os.listdir(data))

X = []      # X is a list of all images
y = []      # y is label of all images 

counter = 0

for file in os.listdir(data):
    image = cv2.imread(data+file)
    X.append(image)
    label = file.split('_')[0]      
    y.append(label)
    if counter > 9:         # if counter is removed
        break               # if counter is removed
    counter += 1            # if counter is removed

# print(len(X) == len(y))     to check if both label and images have equal count
# print(len(X))               # count of images
# print(len(y))               # count of labels


# to comment in a line use  ctrl + /
    