# Platform untuk Mata Kuliah PBP

LINK DEPLOYMENT:
http://andharu-hanif-bingchillingshop.pbp.cs.ui.ac.id/

# TUGAS 2

## Langkah Implementasi (Tugas 2):

1. Buat direktori lokal untuk proyek django dan inisiasi git di dalam direktori tersebut.

2. Buat dan aktifkan virtual environment dengan perintah:

```
python -m venv env
env/Scripts/activate
```

3. Di dalam direktori yang sama, buat berkas requirements.txt dengan isi dependencies:

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

4. Instalasi dependencies dengan perintah:

```

pip install -r requirements.txt

```

5. Inisiasi proyek django dengan perintah:

```

django-admin startproject <nama_proyek> .

```

6. Dalam bagian ALLOWED_HOSTS file settings.py, tambahkan string "localhost" dan "127.0.0.1"

7. Tambah berkas .gitignore dengan isi berkas yang dibutuhkan.
8. Buat direktori main untuk aplikasi main dengan perintah:

```

py manage.py startapp main

```

9. Untuk routing, pertama, tambahkan 'main' di INSTALLED_APPS pada settings.py:

```
INSTALLED_APPS = [
    ...,
    'main',
]
```

10. Lalu, buat berkas urls.py di dalam direktori main.

11. Isi urls.py adalah:

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

12. Di file models.py pada direktori main, saya buat class product, dengan kode sebagai berikut:

```
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    icecreamrating = models.IntegerField()
```

13. Setelah membuat product, saya ingin meletakkan product di file main.html yang nanti akan ditampilkan. Pada views.py, saya membuat fungsi show_main untuk mengembalikan template htmlnya. Kodenya sebagai berikut:

```
def show_main(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, "main.html", context)
```

14. Untuk memetakan fungsi yang dibuat pada views.py, buka urls.py yang di direktori proyek, tambahkan rute URL main dalam urlpatterns:

```
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```

15. Akhirnya, saya deploy ke PWS dengan pertama setup remote origin ke link deployment PWS saya, lalu dilakukan push ke origin pws main. Setelah itu, saya buat file README.md ini.

## Bagan Request Client ke Web Aplikasi Django

![-](image.png)

## Fungsi Git dalam Pengembangan Perangkat Lunak

Fungsi utama Git adalah sebagai version control. Git memungkinkan pengelolaan kode dan versi, serta kolaborasi. Dengan kegunaan tersebut, perubahan kode dapat dilacak dan dengan adanya pencabangan versi proyek, pengelolaan versi kode menjadi lebih mudah, dan kolaborasi dapat dilakukan dengan mengerjakan cabang versi masing-masing tanpa merusak mengubah orang di cabang lainnya. Sehingga Git merupakan alat yang sangat penting dalam pengembangan perangkat lunak.

## Mengapa Django dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?

Saya rasa karena Django termasuk framework fullstack dan juga server-side, kita dapat menyentuh semua sisi pengembangan aplikasi. Mulai dari penanganan interaktivitas sisi klien, hingga interaksi dengan database. Oleh karena itu, menurut saya pembelajaran dengan Django menyeluruh dan membantu membangun fundamental pengembangan aplikasi bagi pembelajarnya.

## Mengapa Model pada Django disebut ORM

Object Relational Mapping (ORM): Sebuah teknik yang digunakan dalam pemrograman untuk menggunakan basisdata relasional sebagai penyimpanan data dengan bentuk objek.
Model pada Django disebut ORM karena Django menggunakan teknik ORM untuk menghubungkan antara objek Python dan basis data relasional.

# TUGAS 3

### Mengapa diperlukan data delivery dalam pengimplementasian sebuah platform

Data delivery diperlukan untuk memastikan informasi atau data dapat dikirim dan diakses dengan efektif antarkomponen dalam sistem atau oleh pengguna.

### XML or JSON?

JSON dikenal lebih populer daripada XML. Mengapa? Sudah diketahui secara luas bahwa JSON memang lebih sederhana dan mudah untuk dibaca, dengan penggunaan key-value pair pada JSON dibandingkan beginning dan end tags pada XML yang lebih kompleks.

### Fungsi is_valid() pada form Django, mengapa dibutuhkan?

Fungsi is_valid() pada form dibutuhkan untuk memvalidasi isi input dari form tersebut.

### Mengapa dibutuhkan csrf_token untuk form

crsf_token berfungsi sebagai lapisan keamanan untuk mencegah serangan. Jika tidak ada csrf_token pada form Django, aplikasinya akan menjadi vulnerable terhadap serangan CSRF. Serangan CSRF (Cross Site Request Forgery) adalah di mana penyerang mengirimkan permintaan tidak sah ke aplikasi atas nama pengguna yang sah tanpa sepengetahuan mereka. Hal itu dapat memungkinkan data pengguna dimanipulasi, account hijacking, dan berbagai dampak buruk lainnya.

## Langkah Implementasi (Tugas 3):

1. Dengan direktori yang tersedia dari tugas sebelumnya, kita lanjut dengan membuat form input data untuk memungkinkan penambahan es krim baru.

Untuk forms, buat file forms.py dalam direktori main, dan tambahkan kode

```
from django.forms import ModelForm
from main.models import Product

class IceCreamEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "icecreamrating"]
```

Dapat dilihat bahwa Product yaitu es krim kita assign ke variabel model, dengan fields berisi atribut-atribut yang sesuai.

Lalu pada views.py kita perlu tambah import redirect dari django.shortcuts.

Masih pada views.py, buat fungsi create_bing_entry yang menerima param request, ini untuk mengambil request user untuk membuat es krim (bing)
baru.

```
def create_bing_entry(request):
    form = IceCreamEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_bing_entry.html", context)
```

Masih dalam views.py, ubah fungsi show_main dari tugas sebelumnya menjadi

```
def show_main(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "main.html", context)
```

Setelah itu, dalam main/urls.py, tambahkan import fungsi create_bing_entry dari main.views. Dan tambahkan path URL fungsinya ke dalam variabel urlpatterns.

Selanjutnya, buat file create_bing_entry.html pada main/templates. Berikut kodenya:

```
{% extends 'base.html' %} {% block content %}
<h1>Add New Ice Cream</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Ice Cream" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

Untuk mendisplay setiap es krim baru yang dibuat dari request user, pada main.html ditambahkan kode berikut:

```
{% if not products %}
    <p>Belum ada ice cream tersedia.</p>
    {% else %}
    <div class="product-list">
      {% for product in products %}
      <div class="product-card">
        <h5>🍦Name</h5>
        <p>{{product.name}}</p>
        <h5>Price</h5>
        <p>{{product.price}} USD</p>
        <h5>Description</h5>
        <p>{{product.description}}</p>
        <h5>Chill Rating</h5>
        <p>{{product.icecreamrating}}/10</p>
        <br />
      </div>
      {% endfor %} {% endif %}
    </div>
    <a href="{% url 'main:create_bing_entry' %}">
      <button>Add Ice Cream</button>
    </a>
    {% endblock content %}
```

Itulah bagaimana implementasi form untuk menambahkan es krim baru dengan request user.

2.  Sekarang, untuk tiap variant es krim, kita ingin menyimpan tersebut menjadi data dalam suatu format tertentu. Terdapat dua opsi yaitu JSON atau XML.

Pada main/views.py, tambahkan import berikut:

```
from django.http import HttpResponse
from django.core import serializers
```

Buatlah fungsi baru untuk menyimpan hasil query dari seluruh data pada Product.

Berikut fungsi untuk kedua formatnya:

```
# Untuk kedua fungsi JSON dan XML persis sama, cuma perlu refactor nama formatnya saja, pada kode di bawah saya tulis <xml/json>.
def show_<xml/json>(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("<xml/json>", data), content_type="application/<xml/json>")
```

Setelah membuat fungsi show_xml dan show_json, tambahkan import baru pada main/urls.py:

```
from main.views import show_main, create_mood_entry, show_xml, show_json
```

Seperti biasa, tambahkan juga path untuk fungsi show_xml dan show_json pada urlpatterns.

Jika kita mau mengakses data pada json atau xml sesuai id, kita dapat buat fungsi baru pada main/views.py. Sama seperti langkah sebelumnya, kita buat dua fungsi berbeda untuk json dan xml namun isinya sama. Hanya diganti namanya saja. Berikut kode fungsinya:

```
def show_<xml/json>_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("<xml/json>", data), content_type="application/<xml/json>")
```

Seperti biasa, tambahkan import show_xml_by_id dan show_json_by_id pada urls.py:

```
from main.views import show_main, create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
```

Tambahkan juga path kedua fungsi tersebut dalam urlpatterns.

Untuk melihat product sesuai id, dapat diakses melalui url http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id].

## SCREENSHOTS:

![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)

# TUGAS 4

### Perbedaan HttpResponseRedirect() dan redirect()

Pada HttpResponseRedirect, argumen pertama hanya bisa url, jadi digunakan jika kita perlu redirect ke URL tertentu dan tidak memerlukan tambahan lainnya. Sedangkan, redirect juga bisa menerima argumen tambahan untuk redirect ke view dan model.

### Cara kerja penghubungan model Product dan User

Pada model Product, ditambahkan variabel

```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

Kode tersebut mengasosiasikan product dengan suatu user.
Potongan kode ForeignKey(...) menunjukkan bahwa setiap produk terhubung dengan satu pengguna (one-to-many), dan jika pengguna dihapus, semua produk yang terkait juga akan dihapus.

### Bagaimana Django mengingat pengguna yang telah login, serta kegunaan lain dari cookies dan apakah semua cookies aman digunakan

Dengan menggunakan cookies, Django menyimpan sesi login user yang di cookie pada browser user.
Kegunaan lain cookies include keamanan, autentikasi dan pengelolaan sesi, menyimpan preferensi user. untuk personalization/advertisement pada pengguna, dan analitik aktivitas user.

## Langkah Implementasi (Tugas 4):

1. Membuat Fungsi Login

   Pertama, pada main/views.py, tambahkan import authenticate dan login dari django.contrib.auth. Lalu, tambahkan fungsi login_user untuk mengautentikasi user yang ingin login.

```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

Pada main/templates, tambahkan berkas HTML baru dengan isi sbb:

```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

Keluar dari views.py dan masuk ke main/urls.py, tambahkan import login_user dari main.views, jangan lupa juga untuk tambahkan url login_user tersebut ke urlpatterns.

```
urlpatterns = [
   ...
   path('login/', login_user, name='login'),
]
```

2. Membuat fungsi logout

Dalam main/views.py, tambahkan import logout dari django.contrib.auth, lalu tambahkan fungsi logout_user sbb:

```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Pada templates/main.html, tambahkan tombol untuk logout di bawh tombol untuk menambah es krim baru.

```
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...
```

Seperti biasa, tambahkan fungsi baru tersebut ke main dengan diimport dulu lalu masukkan pathnya ke urlpatterns.

```
urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
]
```

3. Merestriksi Akses Halaman Main

Pada main/views.py, tambahkan import login_required sbb:

```
from django.contrib.auth.decorators import login_required
```

Setelah langkah ini, pada server lokal, seharusnya sekarang user diredirect ke halaman login daripada langsung melihat daftar es krim.

4. Menggunakan Data dari Cookies

Pada main/views.py, tambahkan import:

```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

Lalu, pada fungsi login_user, tambahkan cookie berupa last_login untuk mengetahui kapan terakhir user melakukan login. Pada block if form.is_valid() tambahan kode berikut:

```
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

Setelah itu, pada context fungsi show_main, tambahkan variabel baru 'last_login' dengan mengambil informasi cookie last_login sbb:

```
context = {
        'name': request.user.username,
        'classroom': classroom,
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }
```

Pada logout_user, kita ubah juga kodenya menjadi berikut:

```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

response.delete_cookie('last_login') berfungsi untuk menghaups cookie last_login saat pengguna melakukan logout.

Kemudian, buka templates/main.html dan tambahkan kode berikut di bawah tombol logout:

```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

5.  Menghubungkan products dengan user secara unik

Buka main/models.py dan tambahkan import user dari django.contrib.auth.models.

Pada model Product yang sudah ada, tambahkan variabel user dengan isinya:

```
class MoodEntry(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ...
```

Penjelasan untuk kode di atas ada pada persoalan pertama tugas ini.

Lalu, buka main/views.py dan ubah kode fungsi create_bing_entry menjadi sbb:

```
form = IceCreamEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_bing_entry.html", context)
```

Setelah itu, ubah value dari product pada fungsi show_main menjadi berikut:

```
def show_main(request):
    mood_entries = MoodEntry.objects.filter(user=request.user)
    context = {
         'name': request.user.username,
         ...
    }
```

Hal ini agar objek product/es krim yang ditampilkan terasosiasikan dengan pengguna yang sedang login.

Value 'name' diganti menjadi request.user.username untuk menampilkan data nama sesuai username pengguna yang sedang login.

Simpan semua perubahan dan lakukan makemigrations. Saat membuat migrasi model, akan muncul error (ini harus terjadi), ketik angka 1 dan enter, lakukan ini dua kali (karena promptnya ada 2).

Setelah sukses, lakukan migrate.

Langkah terakhir, tambahkan import baru pada settings.py yaitu import os, dan ganti variabel DEBUG dari berkas settings.py menjadi:

```
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```
