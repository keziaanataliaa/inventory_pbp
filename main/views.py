from django.shortcuts import render

def show_main(request):
    products = [
        {
            'product_name': 'Cokelat Susu Cadbury Dairy Milk',
            'amount': '50',
            'price': 'Rp 30.000',
            'description': 'Cokelat susu lembut dari Cadbury',
            'brand': 'Cadbury'
        },
        {
            'product_name': 'Cokelat Hazelnut Ferrero Rocher',
            'amount': '60',
            'price': 'Rp 25.000',
            'description': 'Cokelat dengan isi kacang hazelnut dari Ferrero Rocher',
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
