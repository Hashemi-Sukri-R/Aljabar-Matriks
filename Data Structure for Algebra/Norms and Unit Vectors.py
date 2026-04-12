#Soal 1
import numpy as np

# buat vector x dengan ukuran 3x1
x = np.array([ [2], 
               [4], 
               [6]])
print(x)

# hitung nilai L2 norm dari vector x
L2 = (2**2 + 4**2 + 6**2)**(1/2)
print(L2)


#Soal 2
v = np.array([3, 4])
print("\nVektor asli: ", v)

norm = np.linalg.norm(v)
print("Panjang vektor: ", norm)

uv = v / norm
print("Unit vektor: ", uv)

print("Panjang unit vektor: ", np.linalg.norm(uv))