# Logistic Routing Problem

<img src="https://picjumbo.com/wp-content/uploads/white-tir-truck-in-motion-driving-on-highway_free_stock_photos_picjumbo_DSC04205-1080x720.jpg" class="img-responsive" width="50%" height="50%"><img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Luftaufnahmen_Nordseekueste_2013_05_by-RaBoe_tele_46.jpg" class="img-responsive" width="50%" height="50%">

## Tujuan Tugas
1. Review materi pathfinding pada mata kuliah Strategi Algoritma.
2. Mengenal multiple-agent TSP.
3. Melakukan visualisasi data.

## Deskripsi Masalah
Welcome to **Oldenburg** ! Kota kecil cantik ini merupakan sebuah kota kecil di barat lau kota Bremen , Jerman , dengan penduduk kurang lebih 168 ribu jiwa [2018]. Kota kecil ini cocok menjadi lahan uji coba untuk melakukan pemodelan sederhana pembuatan rute pengantaran logistik.<br>
Setiap beberapa jam sekali, sebuah perusahaan logistik akan mengirimkan beberapa kurirnya untuk mengantar barang dari kantor pusat mereka ke beberapa titik tujuan yang tersebar di penjuru kota Oldenburg. Anda diminta untuk mencari rute untuk seluruh kurir sehingga jarak yang ditempuh oleh semua kurir paling kecil, sehingga perusahaan logistik dapat menghemat biaya bensin.

## Library yang digunakan
Pada tugas ini, menggunakan python 3 dan menggunakan beberapa library untuk menyelesaikan milestone yang ada :
1. OpenGL (Visualisasi)
2. Pygame (Visualisasi)
3. MIP (Solver mtsp)

## Instalasi yang diperlukan
Pada tugas ini, saya menggunakan sistem operasi linux ubuntu, untuk dapat menjalankan program ini, perlu melakukan beberapa instalasi sebagai berikut :
1. OpenGL
```
pip3 install PyOpenGL PyOpenGL_accelerate
```
apabila masih belum support, kemungkinan perlu menginstall glut terlebih dahulu, untuk linux, dapat menggunakan command berikut :
```
sudo apt-get install freeglut3-dev
```
2. Pygame
```
pip3 install pygame
```
3. MIP
```
pip3 install mip
```
atau
```
pip3 install mip --user
```
apabila mip tidak dapat dijalankan, karena error "cbclib" is not defined, maka pastikan cbc sudah terinstall, untuk melakukan itu, pada ubuntu dapat menggunakan command :
```
sudo apt-get install -y coinor-cbc
```

## Pendekatan Algoritma
### Pathfinding
Asumsi edge yang disediakan pada dataset adalah dua arah.
Dalam penyelesaian persoalan ini, algoritma pathfinding yang saya gunakan adalah dijkstra. Saya menggunakan algoritma tersebut, karena algoritma tersebut akan mencari jarak terpendek antara dua buah titik berdasarkan suatu titik awalan yang ditentukan. Pemilihan algoritma dijkstra ini juga dikarenakan dengan dijkstra, path dari suatu titik ke titik lain dapat ditelusuri dengan menyimpan informasi parent dari setiap titik. Pembentukan subgraph dan jarak antara titik menggunakan dijkstra ini optimal karena dijkstra akan mencari lintasan terpendek menuju suatu titik berdasarkan edge yang terdapat pada sebuah graf. Jadi, tidak mungkin dijkstra akan menuju sebuah titik pada graf melalui sebuah lintasan yang tidak ada pada graf tersebut. Sehingga, hal ini membuktikan bahwa pathfinding dengan dijkstra sudah optimal karena mencari lintasan terpendek berdasarkan edge yang ada.

### mTSP
Penyelesaian persoalan mTSP pada tugas ini saya menggunakan MIP solver untuk python. Dengan memberikan fungsi objektif minimisasi serta constraint pada persoalan ini, mip solver akan mencari solusi untuk fungsi objektif tersebut se optimal mungkin berdasarkan batas waktu yang diberikan. Pada kasus ini, saya memberikan batas waktu 30 detik. Namun, pada saat saya mencoba untuk langsung penyelesaian mTSP dengan salesman lebih dari 1, MIP tidak menemukan solusi yang optimal maupun feasible, sehingga solusi tidak dapat ditemukan. Maka dari itu, saya mencoba menggunakan pendekatan lain. Pendekatan yang saya gunakan adalah membagi daerah tujuan tiap salesman berdasarkan titik koordinat terhadap titik awal (perusahaan tempat kurir bekerja).

Pendekatan tersebut akan membagi daerah yang kurang lebih jumlah titik tujuan yang akan dikunjungi tiap kurir tersebut sama rata. Hal tersebut didapat dengan mendata banyaknya titik selain perusahaan, kemudian menghitung gradien dari koordinat titik tersebut terhadap koordinat titik perusahaan. Kemudian, titik tersebut akan diurutkan berdasarkan gradien yang telah didapatkan tadi. Lalu, tiap salesman akan dibagi rata jumlah titik tujuan berdasarkan pengurutan titik koordinat berdasarkan gradien. Dengan itu, harapannya adalah pembagian wilayah tersebut dapat memberikan hasil yang optimal, karena setiap titik yang memiliki gradien yang berdekatan akan berada di satu wilayah yang lebih dekat dibanding wilayah lain. 

Kemudian, setelah membagi wilayah untuk tiap kurir tersebut. Akan dijalankan MIP Solver lagi untuk tiap kurir untuk mendapatkan hasil persoalan mTSP yang optimal dengan jumlah salesman sebanyak 1. Pendekatan pathfinding, pembagian wilayah, dan juga solusi MIP solver yang optimal diharapkan akan memberikan hasil yang optimal untuk permasalahan mTSP ini. 

## Cara Menjalankan Program
Untuk menjalankan aplikasi ini, dari root directory project ini dapat pindah ke folder src dengan command "cd src". Kemudian, jalankan file main.py dengan command :
```
cd src
python3 main.py
```
atau apabila python sudah dipastikan dalam versi python 3
dapat menggunakan command
``` 
cd src
python main.py
```
Masukkan untuk kota berupa "OL" atau "SF". OL untuk kota Oldenburg dan SF untuk San Fransisco.


## Bonus
Pada tugas ini, saya dapat menampilkan peta San Fransisco yang lebih besar dengan memanfaatkan zooming serta moving pada OpenGL untuk memperoleh penglihatan pada window OpenGL yang lebih baik.

