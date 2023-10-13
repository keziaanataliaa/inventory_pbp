from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Sum
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    total_amount = items.count()
    jumlah_item = total_amount if total_amount is not None else 0 

    nama_mahasiswa = "Kezia Natalia Theodora N."
    kelas = "PBP C"

    context = {
        'nama_mahasiswa': nama_mahasiswa,
        'kelas': kelas,
        'jumlah_item' : jumlah_item,
        'items': items,
        'last_login': request.COOKIES['last_login'],
        'name': request.user.username,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST, request.FILES)

    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_amount(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == 'GET':
        item.amount += 1
        item.save()
        messages.success(request, 'Jumlah Item Bertambah 1.')
        return redirect('main:show_main')

    return redirect('main:show_main')

def remove_amount(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == 'GET':
        if item.amount > 0:
            item.amount -= 1
            item.save()
            messages.success(request, 'Jumlah Item Berkurang 1.')
        if item.amount == 0:
                item.delete()
        return redirect('main:show_main')

    return redirect('main:show_main')

def delete_product(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == 'GET':
        item.delete()
        messages.success(request, 'Produk berhasil dihapus.')
        return redirect('main:show_main')

    return redirect('main:show_main')

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def get_product_json(request):
    product_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

...
@csrf_exempt
def create_ajax(request):
    print(request.POST)
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        print(product)

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()