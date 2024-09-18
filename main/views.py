from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import IceCreamEntryForm

from .models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "main.html", context)

def create_bing_entry(request):
    form = IceCreamEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_bing_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")