import os
import cv2
import numpy as np
from tensorflow import keras
import tensorflow
from keras import Sequential
from keras.layers import Dense

#------------------------------------------------------------------------------------------------------------------

data = 'Your dataset directory'
print(len(os.listdir(data)))
# print(os.listdir(data))

# countries = ['Malaysia+Indonesia', 'Hungary+Slovakia+Croatia', 'Russia', 
#              'Thailand', 'Portugal+Brazil', 'Japan', 'Spain', 'Armenia', 
#              'Indonesia-Bali', 'Australia', 'Germany']

# These were countries in my dataset


#------------------------------------------------------------------------------------------------------------------

def create_dataset():           # Returns list of image and label list
    global countries
    X = []
    y = []
    img_size = 100              # Image size set to 100*100
    for file in os.listdir(data):
        filename = os.path.join(data, file)
        image = cv2.imread(filename)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (img_size, img_size))
        image = np.array(image, dtype=np.uint32).reshape(img_size*img_size)
        X.append(image)
        label = countries.index(file.split('_')[0])
        y.append(label)
    
    X = np.array(X)
    y = np.array(y)
    return X, y


#------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    X, y = create_dataset()
    network = Sequential()
    network.add(Dense(128, activation = 'relu', input_dim = 10000))
    network.add(Dense(256, activation = 'relu'))
    network.add(Dense(128, activation = 'relu'))
    network.add(Dense(64, activation = 'relu'))
    network.add(Dense(11, activation = 'softmax'))
    network.compile(loss = keras.losses.SparseCategoricalCrossentropy(), 
                    optimizer = 'adam', metrics = 'accuracy')

    network.fit(X, y, epochs=50)