#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.python.keras.callbacks import TensorBoard
import time
import pickle


# In[18]:


x = pickle.load(open("x_t.pickle","rb"))
y = pickle.load(open("y_t.pickle","rb"))


# In[12]:


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


# In[19]:


import matplotlib.pyplot as plt
import numpy as np
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

for i in range(len(x)):
    x[i] = rgb2gray(x[i])
    y[i] = np.int8(y[i])
x = np.array(x)
y = np.array(y)


# In[20]:


plt.imshow(x[3])
print(x[0].shape)
print(y[0].shape)
print(type(y))
print(type(x))


# In[16]:


model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, callbacks=[tf.keras.callbacks.TensorBoard('logs')])
model.evaluate(x, y)


# In[23]:


# Load TENSORBOARD
get_ipython().run_line_magic('load_ext', 'tensorboard.notebook')
# Start TENSORBOARD
get_ipython().run_line_magic('tensorboard', '--logdir logs')


# In[21]:


plt.imshow(x[14])
print(y[14])
model.predict_classes(x)


# In[22]:


model.evaluate(x, y)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




