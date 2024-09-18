# Platform untuk Mata Kuliah PBP

LINK DEPLOYMENT:
http://andharu-hanif-bingchillingshop.pbp.cs.ui.ac.id/

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
