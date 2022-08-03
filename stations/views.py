import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def get_list_from_csv(file):
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        CONTENT = list(reader)
    return CONTENT


def bus_stations(request):
    page_number = int(request.GET.get('page', '1'))
    CONTENT = get_list_from_csv(BUS_STATION_CSV)
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)
