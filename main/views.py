from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Kezia Natalia Thedora N.',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)