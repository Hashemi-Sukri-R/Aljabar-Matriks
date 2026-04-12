#Soal 1
x = 1
print(type(x))

y = 2
print(type(y))
print(x+y)

x_float = 1.5
print(x_float+y)
print(type(x_float))

#Soal 2
import tensorflow as tf

x = tf.constant(1)
print(type(x))

y = tf.constant(2)
print(type(y))

print(tf.add(x, y))

x_float = tf.constant(1.5)
print(tf.add(x_float, tf.cast(y, tf.float32)))

print(type(x_float))

#Soal 3
import torch

x = torch.tensor(1)
print(type(x))

y = torch.tensor(2)
print(type(y))

print(x + y)

x_float = torch.tensor(1.5)
print(x_float + y)

print(type(x_float))