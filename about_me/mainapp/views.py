from django.shortcuts import render, render_to_response, Http404, get_object_or_404, loader, render
from mainapp.models import Work, Hobby, StPlace, Course, Task, Organization
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import datetime
import xml.etree.ElementTree as ET
import urllib.request as urllib


def main(request):
    response = urllib.urlopen('http://www.cbr.ru/scripts/XML_daily.asp')
    html = response.read().decode('cp1251')
    mydoc = ET.fromstring(html)
    res = []
    for child in mydoc:
        if child.find('CharCode').text in ['USD', 'EUR', 'KZT']:
            res.append(
                child.find('CharCode').text + ' ' + child.find('Nominal').text + ' = ' + ' ' + child.find('Value').text)
    return render_to_response('index.html', {'res': res})


def about(request):
    Hob = Hobby.objects.all()
    name = 'павел'
    surmane = 'тупиков'
    middlename = 'андреевич'
    birhday = datetime.date(1991, 7, 8)
    city = 'москва'
    birhday_city = 'омск'
    educations = 'Высшее'
    Phone = '8 966 134 60 99'
    is_hobby_2 = True
    return render_to_response('about.html', {'name': name, 'surmane': surmane, 'middlename': middlename,
                                             'birhday': birhday, 'city': city, 'birhday_city': birhday_city,
                                             'educations': educations, 'Phone': Phone,'is_hobby_2': is_hobby_2,
                                             'Hob': Hob})


def my_study(request):
    st_place = StPlace.objects.all()
    curs_place = Course.objects.all()
    return render_to_response('my_study.html', {'st_place': st_place, 'curs_place': curs_place})


def my_work(request):
    work_place = Work.objects.all()
    return render(request, 'my_work.html', {'work_place': work_place})


def my_project(request):
    graf_place = Task.objects.filter(category='graf')
    din_place = Task.objects.filter(category='din')
    place = Task.objects.filter(category='another')
    return render_to_response('my_project.html', {'graf_place': graf_place, 'din_place': din_place, 'place': place})


def about_mir(request):
    organ = Organization.objects.get(name='НПО МИР')
    return render_to_response('about_organization.html', {'organ': organ})


def about_pil(request):
    organ = Organization.objects.get(name='ФГУП НПЦАП')
    return render_to_response('about_organization.html', {'organ': organ})


def about_urion(request):
    organ = Organization.objects.get(name='НТЦ ЮРИОН')
    return render_to_response('about_organization.html', {'organ': organ})


def about_alfa(request):
    organ = Organization.objects.get(name='ТД Альфа комплект')
    return render_to_response('about_organization.html', {'organ': organ})


def get_works(request):
    if request.is_ajax():
        slice = request.POST['slice']
        print(slice)
        work_place = Work.objects.all()
        if slice:
            work_place = work_place[:int(slice)]
        html = loader.render_to_string('my_work.html', {'work_place': work_place})
        data = {'html': html}
        return JsonResponse(data)
    raise Http404