from django.urls import path
from main.views import show_main, create_bing_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_bing, delete_bing, add_bing_entry_ajax




app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-bing-entry', create_bing_entry, name='create_bing_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-bing/<uuid:id>', edit_bing, name='edit_bing'),
    path('delete/<uuid:id>', delete_bing, name='delete_bing'),
    path('create-bing-entry-ajax', add_bing_entry_ajax, name='add_bing_entry_ajax'),

]   