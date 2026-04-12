#Soal 1
import numpy as np

X = np.array([[5, 2, 1], 
              [3, 7, 4]])
print(X.shape)
print(X[:,0])
print(X[1,:])


#Soal 2
#Pytorch
import torch

X_pt = torch.tensor([[5, 2, 1], 
                     [3, 7, 4]])
print(X_pt.shape)
print(X_pt[:,0])
print(X_pt[1,:])

#Tensorflow
import tensorflow as tf

X_tf = tf.constant([[5, 2, 1], 
                    [3, 7, 4]])
print(X_tf.shape(X_tf))
print(X_tf[:,0])
print(X_tf[1,:])
