import numpy as np

#Soal 1
i = np.array([1, 0])
j = np.array([0, 1])

#bukti bahwa vector i dan vector j itu orthogonal
ortho1 = np.dot(i, j)
if ortho1 == 0:
  print("i dan j orthogonal, karena hasil akhirnya ", ortho1)
else:
  print("i dan j bukan orthogonal, karena hasil akhirnya ", ortho1)


#Soal 2
v = np.array([1, 2])
w = np.array([2, -1])
ortho2 = np.dot(v, w)
if ortho2 == 0:
  print("v dan w orthogonal, karena hasil akhirnya ", ortho2)
else:
  print("v dan w bukan orthogonal, karena hasil akhirnya ", ortho2)