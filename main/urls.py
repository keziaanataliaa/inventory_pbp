from django.urls import path
from main.views import create_product_flutter, show_main
from main.views import show_main, create_product, show_xml
from main.views import show_main, create_product, show_xml, show_json
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from main.views import logout_user
from main.views import add_amount
from main.views import remove_amount
from main.views import delete_product
from main.views import edit_product
from main.views import get_product_json
from main.views import create_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_amount/<int:id>/', add_amount, name='add_amount'),
    path('remove_amount/<int:id>/', remove_amount, name='remove_amount'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]