LINK DEPLOYMENT:
https://andharu-hanif-tokobingchilling.pbp.cs.ui.ac.id/

# Langkah Implementasi Checklist:

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

# Bagan Request Client ke Web Aplikasi Django

![-](image.png)

# Fungsi Git dalam Pengembangan Perangkat Lunak

Fungsi utama Git adalah sebagai version control. Git memungkinkan pengelolaan kode dan versi, serta kolaborasi. Dengan kegunaan tersebut, perubahan kode dapat dilacak dan dengan adanya pencabangan versi proyek, pengelolaan versi kode menjadi lebih mudah, dan kolaborasi dapat dilakukan dengan mengerjakan cabang versi masing-masing tanpa merusak mengubah orang di cabang lainnya. Sehingga Git merupakan alat yang sangat penting dalam pengembangan perangkat lunak.

# Mengapa Django dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?

Saya rasa karena Django termasuk framework fullstack dan juga server-side, kita dapat menyentuh semua sisi pengembangan aplikasi. Mulai dari penanganan interaktivitas sisi klien, hingga interaksi dengan database. Oleh karena itu, menurut saya pembelajaran dengan Django menyeluruh dan membantu membangun fundamental pengembangan aplikasi bagi pembelajarnya.

# Mengapa Model pada Django disebut ORM

Object Relational Mapping (ORM): Sebuah teknik yang digunakan dalam pemrograman untuk menggunakan basisdata relasional sebagai penyimpanan data dengan bentuk objek.
Model pada Django disebut ORM karena Django menggunakan teknik ORM untuk menghubungkan antara objek Python dan basis data relasional.
