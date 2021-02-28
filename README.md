# TUCIL 2 STRATEGI ALGORITMA
-----------------------------------------------------------------    
                     TOPOLOGICAL SORT
-----------------------------------------------------------------
            Created By : M Azhar Faturahman (13519020)

## <--Description-->
Topological Sort adalah suatu metode pengurutan pada graf berarah sehingga didapatkan suatu keterurutan partial linier dari setiap simpulnya yang mana untuk setiap sisi uv dari simpul u ke simpul v, simpul u selalu berada di urutan terdepan daripada simpul v. Topological Sort hanya bisa dilakukan pada suatu graf berarah jika graf berarah tersebut tidak memiliki directed cycle (siklus), graf yang tidak memiliki directed cycle disebut sebagai directed acyclic graph (DAG).

Pada setiap langkah iterasi, algoritma akan melakukan penghapusan simpul dari graf (tahap decrease) atau dalam hal ini membagi permasalah menjadi dua upa-persoalan, simpul yang dihapus dari graf akan dimasukkan ke dalam himpunan solusi, sedangkan graf yang tersisa akan diproses dengan terlebih dahulu menghapus sisi pada suatu simpul yang bertetanggaan dengan simpul yang dihapus (tahap conquer), kemudian langkah diulang hingga didapatkan graf kosong dan proses topological sort selesai.

## <--Built With-->
Python 3.8.5

## <--Usage-->
Cara Penggunaan <Windows 10> :
- Buka folder bin
- Jalankan program `"main.exe"`
- Akan terdapat perintah untuk memasukkan nama file, tulis nama 
  file sesuai dengan yang ada pada folder test lengkap dengan 
  ekstensinya, contoh "test4.txt"
- Program akan otomatis menampilkan solusi yang sesuai.

Alternatif <Windows 10> :
- Buka folder src
- Buka cmd atau powershell pada directory folder src
- Jalankan dengan command `"python 13519020-iteratif.py"` atau
  `"python 13519020-rekursif.py"`
- Akan terdapat perintah untuk memasukkan nama file, tulis nama 
  file sesuai dengan yang ada pada folder test lengkap dengan 
  ekstensinya, contoh "test4.txt"
- Program akan otomatis menampilkan solusi yang sesuai.

## <--Credit-->
Nama  : Muhammad Azhar Faturahman
NIM   : 13519020
Kelas : K01

Tugas Kecil 1 IF2211 Strategi Algoritma
Semester II Tahun 2020/2021