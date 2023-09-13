# inventory_pbp

Link adaptable: https://chocostock.adaptable.app/


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

- Membuat sebuah proyek Django baru.
    Langkah yang saya lakukan untuk membuat proyek Django baru adalah dengan: 
    1. Membuat Direktori dan Mengaktifkan Virtual Environment: membuat direktori untuk proyek Django Anda dan pindah ke dalamnya (nama direktori saya adalah inventory_pbp). Setelah itu, buat dan aktifkan virtual environment untuk memisahkan dependensi proyek ini dari proyek lain dengan menggunakan perintah python -m venv env dan env\Scripts\activate.bat

    2. Menyiapkan Dependencies dan Membuat Proyek Django: Lalu saya buat berkas requirements.txt dan menambahkan beberapa dependencies dan menjalankan virtual environment terlebih dahulu lalu menjalankan perintah pip install -r requirements.txt. Kemudian buka command prompt di direktori di mana ingin membuat proyek Django baru. Kemudian jalankan perintah django-admin startproject inventory_pbp . untuk membuat proyek Django baru dengan nama "inventory_pbp". Pastikan karakter . tertulis di akhir perintah untuk memastikan proyek dibuat dalam direktori saat ini.

    3. Konfigurasi Proyek dan menjalankan server: Buka file settings.py di dalam direktori proyek. Kemudian atur settings.py dengan menambahkan "*" di ALLOWED_HOSTS untuk keperluan deployment. Lalu jalankan server pengembangan dengan perintah python manage.py runserver. Setelah itu proyek Django akan berjalan di server pengembangan dan dapat diakses di http://localhost:8000/

    4. Menghentikan Server dan Menonaktifkan Virtual Environment: Lalu untuk menghentikan server pengembangan, tekan Ctrl + C di terminal tempat server berjalan dan untuk menonaktifkan virtual environment, jalankan perintah deactivate dari dalam direktori proyek.


- Membuat aplikasi dengan nama main pada proyek tersebut.
    Berdasarkan langkah yang sudah dijelaskan di atas, setelah proyek dibuat, maka perlu membuat aplikasi di dalamnya. Aplikasi ini akan memiliki fungsionalitas terkait dengan bagian utama dari proyek dengan menggunakan perintah python manage.py startapp main. Ini akan membuat direktori main dengan struktur dasar aplikasi Django di dalam proyek.

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    Pada langkah ini, buka file urls.py pada level proyek di dalam direktori main (bukan di dalam aplikasi). Tambahkan path baru untuk mengarahkan ke aplikasi 'main' yaitu dengan kode berikut:

    from django.urls import path
    from main.views import show_main
    app_name = 'main'
    urlpatterns = [
        path('', show_main, name='show_main'),
    ]


- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    name sebagai nama item dengan tipe CharField.
    amount sebagai jumlah item dengan tipe IntegerField.
    description sebagai deskripsi item dengan tipe TextField.

    Untuk membuat hal tersebut, buka file models.py di dalam aplikasi 'main' dan tambahkan model 'Item' dengan atribut yang diinginkan. Pada proyek saya, atributnya diantaranya adalah product_name, amount, description, price, dan brand. Lalu masing-masing atribut dibuat kedalam tipe data yang sesuai seperti CharField, DateField, IntegerField, dan TextField.


- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    Fungsi show_main mengambil parameter request, yang merupakan objek permintaan HTTP dari pengguna. Di dalamnya, terdapat dua variabel products, yang berisi informasi tentang produk-produk dalam bentuk dictionary (product_name, amount, description, price, dan brand). Selain itu, terdapat dua variabel tambahan nama_mahasiswa dan kelas yang berisi nama dan kelas mahasiswa. Selanjutnya, data-data ini diorganisir dalam sebuah context, yang akan diteruskan ke template. context terdiri dari tiga kunci, yaitu 'items' yang berisi produk-produk, 'nama_mahasiswa', dan 'kelas'. Terakhir, fungsi render digunakan untuk merender tampilan. Fungsi ini membutuhkan tiga argumen: request yang mewakili permintaan pengguna, "main.html" sebagai nama template yang akan digunakan, dan context yang mengandung data yang akan ditampilkan di tampilan HTML.
 

- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    Membuat pengaturan rute pada berkas urls.py di aplikasi utama untuk menetapkan fungsi yang telah didefinisikan di views.py. Selanjutnya, tambahkan entri di berkas urls.py di direktori proyek dengan mengimpor fungsi include dari django.urls. Rute URL dari aplikasi lain dapat diarahkan menuju tampilan utama melalui variabel urlpatterns.

- Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    Pertama, buatlah akun di Adaptable dan hubungkan akun tersebut dengan akun GitHub. Selanjutnya, buat aplikasi baru dan sambungkan dengan repositori GitHub yang sudah ada dengan memilih opsi "All Repositories" selama proses instalasi. Setelah itu, pilih repositori yang ingin di-deploy ke Adaptable, yaitu inventory_pbp. Gunakan Python App Template sebagai template deployment dan tentukan PostgreSQL sebagai tipe basis data yang akan digunakan. Pastikan versi Python sesuai dengan spesifikasi aplikasi dengan memeriksa versi Python melalui virtual environment dan menjalankan perintah "python --version". Tambahkan "python manage.py migrate && gunicorn inventory_pbp.wsgi" di bagian "Start Command". Selanjutnya, tentukan nama aplikasi yang akan menjadi domain untuk situs web aplikasi dan aktifkan HTTP Listener on PORT. Terakhir, klik tombol "Deploy App" dan proses deployment akan dimulai. Setelah proses selesai, maka sudah dapat mengakses aplikasi melalui Internet.

Tambahan:
- Melakukan testing Django (bisa dilakukan saat akhir)
    Saya melakukan 2 testing Django. Pertama, test_main_url_is_exist untuk menguji ketersediaan URL '/main/' dengan melakukan permintaan HTTP GET. Pengujian ini memeriksa apakah server memberikan respons dengan status kode 200, menunjukkan bahwa URL tersebut dapat diakses. Kedua, test_main_using_main_template memeriksa apakah tampilan menggunakan template 'main.html'. Dengan melakukan permintaan HTTP GET ke '/main/', pengujian ini memastikan bahwa tampilan mengakses template yang benar.

- Add, Push, dan Commit ke dalam Repositori GitHub (bisa dilakukan diawal setelah membuat direktori, ditengah, ataupun diakhir)
    Saya membuat repositori baru di GitHub dengan nama "inventory_pbp". Selanjutnya, saya membuat direktori baru dan menginisiasi penggunaan Git untuk menghubungkannya dengan repositori di GitHub. Selanjutnya dilakukan add, push, dan commit untuk setiap perubahan yang dilakukan agar selalu terupdate.



## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![alt text](bagan.jpg)

Alur permintaan dari client ke aplikasi web berbasis Django dimulai dengan pengguna mengajukan permintaan melalui antarmuka pengguna. Permintaan tersebut akan diteruskan melalui berkas urls.py, di mana pola URL akan dicocokkan. Setelah pencocokan berhasil, Django akan menunjuk ke view yang sesuai yang telah didefinisikan di views.py dan menjalankan fungsi views sesuai dengan yang direquest oleh client. Views kemudian dapat membutuhkan akses ke database, dalam hal ini, akan memanggil query ke models.py dan models.py mengambil data dari database. Hasil dari query akan dikirimkan kembali ke views untuk diproses lebih lanjut. Setelah proses permintaan selesai, hasilnya akan dimasukkan ke dalam berkas HTML yang sesuai dalam template. Terakhir, halaman web yang dihasilkan akan dikirimkan sebagai respon kembali kepada client


## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan dalam pengembangan perangkat lunak Python untuk mengisolasi paket dan dependensi dari suatu aplikasi. Hal ini penting karena memungkinkan pengembang untuk bekerja pada berbagai proyek dengan dependensi yang mungkin berbeda-beda tanpa terjadi konflik. Dengan menggunakan virtual environment, pastikan bahwa setiap proyek memiliki akses terhadap versi paket yang spesifik sesuai kebutuhan, tanpa mempengaruhi atau berinterferensi dengan proyek lain atau dengan versi package sistem.

Meskipun memungkinkan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun tidak disarankan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Hal ini karena tanpa virtual environment, ada risiko terjadinya konflik versi dan masalah dependensi. Proyek Python yang berbeda mungkin memerlukan versi paket yang berbeda, dan tanpa isolasi yang diberikan oleh virtual environment, ini dapat menyebabkan kegagalan atau kerusakan pada proyek. Dengan menggunakan virtual environment, pengembang dapat menciptakan lingkungan pengembangan yang terisolasi, meminimalkan risiko konflik, dan memastikan stabilitas serta konsistensi proyek Python. Oleh karena itu, penggunaan virtual environment adalah praktik terbaik dalam pengembangan Python.


## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Penjelasan terkait apa itu MVC, MVT, dan MVVM:
- MVC:
    Model-View-Controller (MVC) adalah sebuah pola desain arsitektural yang digunakan dalam pengembangan perangkat lunak. Dalam MVC, aplikasi terbagi menjadi tiga komponen utama:
    - Model: Bertanggung jawab untuk mengelola data dan logika aplikasi. Ini mendefinisikan struktur data dan berurusan dengan operasi terkait data. Model juga tidak memiliki pengetahuan tentang tampilan atau pengguna yang memanfaatkannya.
    - View: Menampilkan data dari Model dan menghubungkannya dengan template atau antarmuka pengguna. View bertugas untuk mengatur tampilan dan mempresentasikan informasi kepada pengguna. Namun, View tidak menangani logika bisnis atau manipulasi data.
    - Controller: Bertindak sebagai perantara antara Model dan View. Controller menangani input dari pengguna, memprosesnya (biasanya dengan memanipulasi Model), dan memperbarui tampilan (View) sesuai dengan hasil dari proses tersebut.
    MVC memisahkan tanggung jawab antara tampilan, logika aplikasi, dan data, sehingga memungkinkan pengembang untuk bekerja secara terpisah pada setiap komponen. Hal ini menghasilkan kode yang lebih terstruktur, mudah dikelola, dan memungkinkan penggunaan kembali komponen-komponen tertentu dalam aplikasi yang berbeda.

- MVT:
    Konsep Model-View-Template (MVT) adalah struktur dasar yang sangat penting dalam pengembangan aplikasi web menggunakan framework Django di bahasa pemrograman Python. MVT membagi tugas utama dalam pengembangan menjadi tiga komponen utama: Model, View, dan Template. 
    - Model: berperan sebagai wadah untuk data dan logika aplikasi, memfasilitasi koneksi dengan basis data dan manipulasi data. 
    - View: bertanggung jawab atas logika presentasi, memproses permintaan dari pengguna, dan menyiapkan data untuk ditampilkan di antarmuka pengguna. 
    - Template: berfungsi untuk mendefinisikan tampilan antarmuka pengguna. 
    MVT akan berguna untuk mengembangkan dalam merancang aplikasi web yang terstruktur, mudah dikelola, serta memungkinkan penggunaan kembali kode dalam berbagai bagian aplikasi. MVT memungkinkan pemisahan tugas yang jelas antara Model, View, dan Template. Ini memungkinkan pengembang untuk bekerja pada setiap komponen secara terpisah. Selain itu, MVT juga memfasilitasi penggunaan kembali kode di berbagai bagian aplikasi, menghemat waktu dan sumber daya pengembangan. Dengan struktur MVT, pengembang dapat merancang aplikasi yang lebih terstruktur, mudah dikelola, serta siap untuk berkembang mengikuti kebutuhan yang berubah.

- MVVM:
    Konsep Model-View-ViewModel (MVVM) adalah sebuah arsitektur perangkat lunak yang sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna, terutama dalam konteks pengembangan aplikasi berbasis framework seperti WPF (Windows Presentation Foundation) untuk aplikasi desktop dan Xamarin untuk pengembangan aplikasi lintas platform. MVVM membagi aplikasi menjadi tiga komponen utama:
    - Model: Mirip dengan konsep MVT, Model dalam MVVM bertanggung jawab untuk mengelola data dan logika bisnis. Ini mewakili struktur data dan mengatur interaksi dengan basis data atau sumber data lainnya.
    - View: View dalam MVVM adalah antarmuka pengguna yang menampilkan data dan berinteraksi dengan pengguna. Ini mencakup elemen UI seperti tombol, formulir, dan elemen tampilan lainnya.
    - ViewModel: ViewModel adalah komponen penting yang membedakan MVVM dari MVT. ViewModel berperan sebagai penghubung antara Model dan View. Ini mengambil data dari Model dan mempersiapkannya agar sesuai untuk ditampilkan di View. ViewModel juga

Perbedaan MVC, MVT, dan MVVM:
![alt text](tabel_perbedaan.png)



Referensi:
- https://www.guru99.com/mvc-vs-mvvm.html
- https://levelup.gitconnected.com/mvc-vs-mvp-vs-mvvm-35e0d4b933b4
- https://pbp-fasilkom-ui.github.io/ganjil-2024/
- https://www.geeksforgeeks.org/python-virtual-environment/




    



        
