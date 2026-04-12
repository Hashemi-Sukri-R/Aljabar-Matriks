#Soal 1

import numpy as np

x = np.array([[1],
              [2],
              [3]])

print("Panjang vector x:", x.size)

print("Ukuran vector x:", x.shape)

print("Tipe data vector x:", type(x))

elemen_pertama = x[0, 0]
print("Elemen pertama:", elemen_pertama)

print("Tipe data elemen pertama:", type(elemen_pertama))



#Soal 2
x_t = x.transpose()
print("\nUkuran vector x_t: ", x_t.shape)

y = np.array([[3, 4, 5]])
y_t = y.transpose()
print("Vector y_t setelah ditrasnpose: \n", y_t)



#Soal 3

#Pytorch
print("\nMenggunakan Torch:")
import torch as pt

x_t = x.transpose()
print("Ukuran vector x_t:", x_t.size)

y = pt.tensor([[3, 4, 5]])
y_t = y.t()
print("Vector y_t setelah transpose:\n", y_t)

#Tensorflow
print("\nMenggunakan Tensorflow:")
import tensorflow as tf

x_t = tf.transpose(x)
print("Ukuran vector x_t:", x_t.shape)

y = tf.constant([[3, 4, 5]])
y_t = tf.transpose(y)
print("Vector y_t setelah ditranspose:\n", y_t.numpy())