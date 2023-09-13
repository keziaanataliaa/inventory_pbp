from django.shortcuts import render

def show_main(request):
    products = [
        {
            'product_name': 'Cokelat Susu Cadbury Dairy Milk',
            'amount': '50',
            'price': 'Rp 30.000',
            'description': 'Cokelat susu lembut dari Cadbury, memberikan pengalaman rasa yang lezat dan memuaskan',
            'brand': 'Cadbury'
        },
        {
            'product_name': 'Dark Chocolate Lindt',
            'amount': '40',
            'price': 'Rp 40.000',
            'description': 'Dark Chocolate Lindt memiliki rasa kaya dan intens. Dibuat dari biji kakao berkualitas tinggi, memberikan pengalaman cokelat hitam yang otentik dan memuaskan',
            'brand': 'Lindt'
        },
        {
            'product_name': 'Cokelat Milk Chocolate Hersheys',
            'amount': '70',
            'price': 'Rp 20.000',
            'description': 'Cokelat Milk Chocolate Hersheys adalah pilihan klasik untuk penggemar cokelat susu',
            'brand': 'Herseys'
        },
        {
            'product_name': 'Cokelat Hazelnut Ferrero Rocher',
            'amount': '60',
            'price': 'Rp 25.000',
            'description': 'Cokelat dengan isi kacang hazelnut dari Ferrero Rocher, menyajikan rasa kacang yang lezat dalam setiap gigitan.',
            'brand': 'Ferrero Rocher'
        }
    ]

    nama_mahasiswa = "Kezia Natalia Theodora N."
    kelas = "PBP C"

    context = {
        'items': {'products': products},
        'nama_mahasiswa': nama_mahasiswa,
        'kelas': kelas
    }

    return render(request, "main.html", context)
