# inventory_pbp

Link adaptable: https://chocostock.adaptable.app/

## TUGAS 3
## Apa perbedaan antara form POST dan form GET dalam Django?
![alt text](tabel_perbedaan_POST_GET.png)

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

Dalam konteks pengiriman data, XML dan JSON umumnya digunakan untuk mengirim dan menyimpan data, sementara HTML digunakan untuk mengatur dan menampilkan konten di browser. Pemilihan format tergantung pada kebutuhan dan penggunaan spesifik dari data yang akan dikirim atau disimpan. 
- XML (eXtensible Markup Language):
    - Tujuan Utama: XML digunakan untuk menyimpan dan mempertukarkan data terstruktur antar sistem. Ini memungkinkan untuk mendefinisikan struktur data khusus sesuai kebutuhan.
    - Keunggulan: Cocok untuk data yang kompleks dan terstruktur dengan kebutuhan validasi yang ketat. Dapat digunakan dalam berbagai konteks seperti konfigurasi, pertukaran data, dan penyimpanan terstruktur.
    - Kekurangan: Lebih berat dan kompleks dalam hal sintaksis, memerlukan lebih banyak karakter untuk mendefinisikan elemen dan struktur data. 

- JSON (JavaScript Object Notation):
    - Tujuan Utama: JSON terutama digunakan untuk pertukaran data di lingkungan yang lebih ringan dan efisien seperti web dan aplikasi seluler. Ini adalah format data ringan yang memanfaatkan sintaksis JavaScript.
    - Keunggulan: Lebih ringan dan lebih efisien dalam hal ukuran file dan penggunaan bandwidth. Memiliki format yang lebih mudah dibaca oleh manusia dan lebih mudah diproses oleh mesin.
    - Kekurangan: Tidak mendukung validasi bawaan, membutuhkan pendekatan manual untuk memastikan data sesuai dengan struktur yang diinginkan. 
    
- HTML (HyperText Markup Language):
    - Tujuan Utama: HTML digunakan untuk membuat struktur dan tata letak halaman web, serta menentukan cara konten disajikan di browser.
    - Keunggulan: Cocok untuk menampilkan konten dan interaksi pengguna di browser. Memiliki kemampuan bawaan untuk menampilkan gambar, video, tautan, formulir, dan elemen UI lainnya.
    - Kekurangan: Fokus utama pada presentasi dan tata letak, bukan penyimpanan atau pertukaran data terstruktur.


## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Kesederhanaan dan Keterbacaan (Simplicity and Readability):
    JSON menggunakan struktur data yang sederhana dan mudah dipahami oleh manusia. Data disusun dalam format teks yang terorganisir dengan baik, membuatnya mudah untuk dibaca dan diinterpretasikan oleh pengembang dan mesin.

- Kesesuaian dan Interoperabilitas (Compatibility and Interoperability):
    JSON adalah format yang independen dari bahasa dan platform. Hal ini memungkinkan aplikasi yang ditulis dalam bahasa pemrograman yang berbeda untuk berkomunikasi dan bertukar data dengan mudah tanpa masalah kompatibilitas.

- Kinerja dan Efisiensi (Performance and Efficiency):
    JSON memiliki ukuran yang kecil dibandingkan dengan format pertukaran data lain seperti XML. Ini mengakibatkan pengiriman dan penerimaan data yang lebih cepat, menghemat waktu dan sumber daya jaringan.

- Keamanan dan Validasi (Security and Validation):
    JSON memungkinkan penggunaan metode validasi dan sanitasi data untuk memastikan bahwa data yang diterima adalah data yang benar dan aman. Pengguna dapat menerapkan kontrol keamanan tambahan seperti enkripsi untuk melindungi data.

- Fleksibilitas dan Ekstensibilitas (Flexibility and Extensibility):
    JSON mendukung struktur data yang fleksibel, memungkinkan pengembang untuk menyesuaikan format data sesuai dengan kebutuhan spesifik aplikasi. Jika diperlukan, dapat dengan mudah menambahkan atau mengubah atribut data tanpa mempengaruhi kompatibilitas dengan aplikasi lain.

- Kesesuaian dan Interoperabilitas (Compatibility and Interoperability):
    JSON kompatibel dengan sebagian besar bahasa pemrograman dan platform. Ini memungkinkan aplikasi yang ditulis dalam bahasa yang berbeda untuk saling berkomunikasi dan bertukar data tanpa mengalami kendala kompatibilitas.



## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat input form untuk menambahkan objek model pada app sebelumnya.
    1. Mengatur Routing dari main/ ke /
        - Buka berkas urls.py pada folder inventory_pbp.
        - Ubah path main/ menjadi '' pada urlpatterns.
        - Simpan perubahan dan jalankan server dengan perintah python manage.py runserver.
    2. Implementasi Skeleton sebagai Kerangka Views
        - Buat folder "templates" pada root folder.
        - Buat berkas base.html dengan kode template dasar yang telah disediakan.
        - Sesuaikan pengaturan TEMPLATES di berkas settings.py agar base.html terdeteksi sebagai berkas template.
        - Ubah kode berkas main.html pada direktori main menjadi menggunakan base.html sebagai template utama.
    3. Membuat Form Input Data dan Menampilkan Data Produk Pada HTML
        - Buat berkas forms.py pada direktori main untuk membuat struktur form ProductForm.
        - Buka berkas views.py di folder main dan tambahkan import yang diperlukan.
        - Tambahkan fungsi create_product untuk menangani form input data produk.
        - Modifikasi fungsi show_main untuk mengambil semua objek Product.
        - Tambahkan path URL untuk create_product di berkas urls.py di main.
        - Buat berkas create_product.html untuk menampilkan form input data produk.
    4. Menggunakan Form Input Data
        - Pada halaman utama, tampilkan data produk dalam bentuk tabel.
        - Tambahkan tombol "Add New Product" yang akan mengarahkan ke halaman form input data pada berkas main.html


- Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID dan Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

    1. Menambahkan data dengan format HTML
        - Membuat folder templates di dalam direktori main
        - Di dalam folder templates, buat berkas HTML dan tambahkan kode HTML untuk menampilkan daftar produk.

    2. Mengembalikan Data dalam Bentuk XML
        - Buka views.py pada folder main.
        - Tambahkan import HttpResponse dan serializers di bagian paling atas.
        - Buat fungsi show_xml(request) untuk menampilkan data dalam format XML.
        - Di dalam fungsi show_xml, ambil semua data dari model Product.
        - Gunakan serializers.serialize() untuk mengubah data menjadi format XML.
        - Kembalikan response dengan parameter data hasil serialisasi dan tipe konten "application/xml".
        - Buka urls.py pada folder main dan impor fungsi yang baru saja dibuat.
        - Tambahkan path URL untuk mengakses fungsi show_xml.

    3. Mengembalikan Data dalam Bentuk JSON
        - Buka views.py pada folder main.
        - Tambahkan fungsi show_json(request) untuk menampilkan data dalam format JSON.
        - Di dalam fungsi show_json, ambil semua data dari model Product.
        - Gunakan serializers.serialize() untuk mengubah data menjadi format JSON.
        - Kembalikan response dengan parameter data hasil serialisasi dan tipe konten "application/json".
        - Buka urls.py pada folder main dan impor fungsi yang baru saja dibuat.
        - Tambahkan path URL untuk mengakses fungsi show_json.

    4. Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON
        - Buka views.py pada folder main.
        - Tambahkan dua fungsi baru, show_xml_by_id(request, id) dan show_json_by_id(request, id), untuk menampilkan data berdasarkan ID dalam format XML dan JSON.
        - Di dalam kedua fungsi tersebut, ambil data dari model Product berdasarkan ID.
        - Gunakan serializers.serialize() untuk mengubah data menjadi format XML atau JSON tergantung pada fungsi yang dipanggil.
        - Kembalikan response dengan parameter data hasil serialisasi dan tipe konten yang sesuai (XML atau JSON).
        - Buka urls.py pada folder main dan impor fungsi yang baru saja dibuat.
        - Tambahkan path URL untuk mengakses fungsi show_xml_by_id dan show_json_by_id dengan menyertakan parameter ID.


Referensi:
- https://docs.djangoproject.com/en/4.2/topics/forms/#:~:text=GET%20and%20POST&text=Django's%20login%20form%20is%20returned,this%20to%20compose%20a%20URL.
- https://www.w3schools.com/tags/ref_httpmethods.asp
- https://www.guru99.com/json-vs-xml-difference.html
- https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/
- https://www.linkedin.com/advice/3/what-benefits-drawbacks-using-json-data#:~:text=One%20of%20the%20main%20benefits,data%20format%20for%20web%20applications.
- https://brandmed.com/blog/development/the-power-of-json-whats-behind-the-popularity
- https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-2 


## Screenshot hasil akses URL pada Postman

- HTML
![alt text](html.png)

- XML
![alt text](xml.png)

- JSON
![alt text](json.png)

- XML by ID
![alt text](xmlbyid.png)

- JSON by ID
![alt text](jsonbyid.png)



## TUGAS 2
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
    Konsep Model-View-Template (MVT) adalah struktur dasar yang sangat penting dalam pengembangan aplikasi web menggunakan framework Django di bahasa pemrograman Python. MVT membagi tugas utama dalam pengembangan menjadi tiga komponen utama: 
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




    



        
