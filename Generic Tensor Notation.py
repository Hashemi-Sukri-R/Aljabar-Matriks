#Soal 1
#jelaskan tentang perintah ini
#images_pt = torch.zeros([32, 28, 28, 3])

import torch

images_pt = torch.zeros([32, 28, 28, 3])
"""**PENJELASAN**

1. torch.zeros(...)
-Membuat semua tensor berisi angka 0

2. [32, 28, 28, 3]
- 32 : Jumlah data (biasanya jumlah gambar / batch size)
- 28 : Tinggi gambar (height)
- 28 : Lebar gambar (width)
- 3 : Jumlah channel warna (RGB)

Perintah ini membuat sebuah tensor berukuran 32 gambar, 
di mana setiap gambar memiliki ukuran 28×28 piksel dengan 3 channel warna (RGB), 
dan semua nilainya diinisialisasi dengan 0 (hitam).

Itulah kenapa setiap angka yang muncul di outputnya adalah 0, 
karena dari perintahnya adalah membuat tensor berisi angka 0
"""