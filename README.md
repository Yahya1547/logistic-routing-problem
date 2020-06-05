# Logistic Routing Problem

<img src="https://picjumbo.com/wp-content/uploads/white-tir-truck-in-motion-driving-on-highway_free_stock_photos_picjumbo_DSC04205-1080x720.jpg" class="img-responsive" width="50%" height="50%"><img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Luftaufnahmen_Nordseekueste_2013_05_by-RaBoe_tele_46.jpg" class="img-responsive" width="50%" height="50%">

## Tujuan Tugas
1. Review materi pathfinding pada mata kuliah Strategi Algoritma.
2. Mengenal multiple-agent TSP.
3. Melakukan visualisasi data.

## Deskripsi Masalah
Welcome to **Oldenburg** ! Kota kecil cantik ini merupakan sebuah kota kecil di barat lau kota Bremen , Jerman , dengan penduduk kurang lebih 168 ribu jiwa [2018]. Kota kecil ini cocok menjadi lahan uji coba untuk melakukan pemodelan sederhana pembuatan rute pengantaran logistik.<br>
Setiap beberapa jam sekali, sebuah perusahaan logistik akan mengirimkan beberapa kurirnya untuk mengantar barang dari kantor pusat mereka ke beberapa titik tujuan yang tersebar di penjuru kota Oldenburg. Anda diminta untuk mencari rute untuk seluruh kurir sehingga jarak yang ditempuh oleh semua kurir paling kecil, sehingga perusahaan logistik dapat menghemat biaya bensin.

## Multiple-Agent TSP
Masalah pengantaran barang untuk satu kendaraan dengan fungsi objektif jarak minimal dapat dimodelkan oleh Travelling Salesman Problem. Akan tetapi, perusahaan logistik biasanya memiliki lebih dari satu kendaraan yang berangkat bersamaan, sehingga TSP kurang cocok digunakan. Generalisasi TSP untuk beberapa agen adalah **multiple-agent TSP (mTSP)**, dan model masalah ini akan kita gunakan. Pada mTSP, akan terdapat *m* tur yang akan dibangun. Syarat dari semua tur mirip dengan TSP, yaitu bahwa seluruh tur akan kembali ke simpul awal (mewakili kantor pusat) dan setiap tujuan hanya akan dilewati oleh satu tur.

## Tugas
Kita akan menggunakan dataset jalanan pada kota Oldenburg yang dapat diakses pada <a href="https://www.cs.utah.edu/~lifeifei/SpatialDataset.htm">tautan ini.</a> Lakukan pengunduhan untuk kedua data jalanan di kota Oldenburg. Data pertama merupakan koordinat simpul, data kedua merupakan data sisi antar simpul. Asumsikan seluruh jalan dua arah.<br> 
Seperti yang disebutkan sebelumnya, kita akan menggunakan pendekatan mTSP dalam permasalahan ini. Untuk mempermudah anda dan mempermudah penilaian, tugas akan dibagi dalam beberapa tahap.

### Milestone 1
Pada milestone 1, anda diminta untuk membangun sebuah upagraf dari graf jalan keseluruhan kota Oldenburg. Upagraf tersebut merupakan sebuah graf lengkap tak berarah, dengan simpul-simpulnya adalah titik tujuan pengiriman barang ditambah titik yang mewakili kantor pusat perusahaan logistik. Simpul-simpul tersebut merupakan masukan program yang dimasukkan oleh pengguna, dengan format masukan bebas. Hasilkan sebuah matriks jarak antar simpul upagraf lengkap. Nilai untuk milestone pertama maksimal adalah **600**.

### Milestone 2
Pada Milestone 2 , anda akan menggunakan upagraf yang telah dihasilkan pada Milestone 1 untuk membangun rute dari para kurir dengan pendekatan mTSP. Tampilkan rute yang diambil oleh tiap kurir. Nilai maksimal pada milestone kedua adalah **1500**

### Milestone 3
Setelah berhasil mendapatkan rute bagi para kurir, selanjutnya anda diminta untuk menggambarkan rute dari para kurir. Visualisasi rute  minimal membedakan warna rute untuk tiap kurir dan menampilkan upagraf yang digunakan untuk membuat rute. Nilai lebih akan diberikan jika anda dapat menampilkan rute beserta seluruh peta jalan di kota Oldenburg. Nilai minimal adalah **800** dan nilai maksimal adalah **1500**

## Pengerjaan
Tugas ini individual.<br>
Lakukan *fork* terhadap *repository* ini.<br>
Spek tugas cukup umum, sehingga asisten tidak membatasi algoritma maupun bahasa pemrograman yang digunakan, walaupun **penggunaan Python disarankan**. Algoritma yang digunakan untuk pathfinding harus optimal, namun hasil dari mTSP tidak harus optimal (*Note : beberapa pustaka optimization bisa menghasilkan solusi sub-optimal dalam batas waktu tertentu*). Bila merasa sudah menyelesaikan tugas, silahkan lakukan pull request dan hubungi asisten lewat email untuk melakukan demo.<br>
Pastikan ada menambahkan/menggati README ini saat mengumpulkan. README minimal mengandung :

1. Pendekatan algoritma yang digunakan untuk pathfinding dan penyelesaian mTSP, serta 
2. Cara menjalankan program, termasuk instalasi pustaka bila menggunakan bermacam pustaka

Anda bebas menggunakan pustaka maupun referensi apapun untuk mengerjakan tugas, kecuali kode/pustaka jadi yang melakukan *routing*, karena tujuan tugas adalah membuat sebuah prototipe pembuatan rute. Pastikan anda mencantumkan sumber bilamana anda menggunakan kode dari orang lain. Akan tetapi, pemahaman terhadap solusi masalah menjadi bagian penting dari penilaian , sehingga anda disarankan untuk menuliskan kode anda sendiri.<br>

## Penilaian
Nilai maksimal non-bonus adalah **4200**. Penilaian akan dilakukan berdasarkan : 
1. kode sumber,
2. pendekatan solusi, 
2. demo aplikasi dan ,
3. pemahaman terhadap solusi masalah.

Untuk poin (1) dan poin (2) , nilai maksimal adalah **3600** dari ketiga milestone.<br> 
Demo hanya dapat dilakukan sekali. Demo bernilai **600** poin. Pada demo, anda akan menunjukkan hasil aplikasi dan akan terdapat tanya jawab untuk menguji pemahaman.<br>
Asisten juga akan menjalankan **plagiarism checking** antar kode sumber peserta. Bila ditemukan adanya kecurangan, maka nilai peserta bersangkutan adalah 0 tanpa pengubahan, dan pengurangan poin maksimal tidak akan berlaku. Perhatikan bahwa selama anda mencantumkan asal kode yang anda salin , tidak menggunakan pustaka untuk *routing* dan tidak menyalin kode milik teman anda, anda tidak akan mendapat masalah.

## Bonus
Bonus **300** poin diberikan jika anda dapat mengirimkan hasil algoritma beserta beberapa contoh masukan/keluaran untuk kasus kota San Francisco , dengan jumlah jalanan yang lebih besar dari Kota Oldenburg. Dataset dapat diambil di website yang sama.

## Kontak
Silahkan hubungi asisten lewat line @alamhasabiebaru atau lewat email 13517096@std.stei.itb.ac.id dengan subjek diawal tulisan \[SELEKSI IRK\] . *Note : waktu menjawab bervariasi, namun email biasanya akan dibalas kurang dari sehari. Line mungkin tidak dibalas dalam waktu satu-dua hari. Mohon bersabar :)*. Pertanyaan juga dipersilahkan. Jawaban akan diposting dalam bagian QnA README ini.

## QnA
- Bagaimana penentuan upagraf ? Apakah bebas oleh developer ?<br>
Upagraf dibangun dari masukan simpul-simpul tujuan dan simpul kantor pusat. Masukan tersebut berasal dari pengguna, namun developer bebas menentukan format masukan simpul.

## Referensi
Silahkan gunakan referensi berikut sebagai awal pengerjaan tugas:<br>
[1] Dataset : https://www.cs.utah.edu/~lifeifei/SpatialDataset.htm<br>
[2] Pengenalan dan formulasi mTSP : https://neos-guide.org/content/multiple-traveling-salesman-problem-mtsp<br>
[3] MIP , pustaka Python untuk optimisasi : https://python-mip.readthedocs.io/en/latest/intro.html<br>
[4] OpenGL untuk Python : https://stackabuse.com/brief-introduction-to-opengl-in-python-with-pyopengl/<br>
[5]  Li, Feifei, Dihan Cheng, Marios Hadjieleftheriou, George Kollios, and Shang-Hua Teng. "On trip planning queries in spatial databases." In International symposium on spatial and temporal databases, pp. 273-290. Springer, Berlin, Heidelberg, 2005.

## Credits
Thank you for Li Fei Fei et. al. for providing the data.


## installation
pip install PyOpenGL PyOpenGL_accelerate
sudo apt-get install freeglut3-dev
pip3 install pygame

pip install mip
atau
pip install mip --user
