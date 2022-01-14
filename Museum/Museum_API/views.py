from django.http import HttpResponse
from django.shortcuts import render
from .models import APIS
from datetime import date, datetime
from rest_framework import routers, serializers, viewsets
import sqlite3
import requests
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST.get('depname'):
            dep_code = request.POST.get('depname')
            url_txt = 'https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=' + dep_code + \
                      '&q=cat'

            r = requests.get(url_txt)
            data = r.text
            parse_json = json.loads(data)
            parse_json = parse_json['objectIDs']
            new_obj = []
            for i in parse_json:
                r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(i))
                data = r.text
                parse_json = json.loads(data)
                new_obj.append(parse_json)


            final_dict = {}
            for j in range(len(new_obj)):
                final_dict[new_obj[j]['objectID']] = new_obj[j]['artistDisplayName'] + ' - ' + new_obj[j]['title']


            return render(request, 'arts.html', {'authors': final_dict})

        elif request.POST.get('image_id'):
            image_id = request.POST.get('image_id')
            url_txt = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(image_id)
            r = requests.get(url_txt)
            data = r.text
            parse_json = json.loads(data)
            parse_json = parse_json['primaryImage']
            return render(request, 'images.html', {'value': parse_json})
    else:
        r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/departments')
        r_status = r.status_code
        data = r.text
        parse_json = json.loads(data)
        parse_json = parse_json['departments']
        department_dict = {}
        keys = []
        values = []

        for i in parse_json:
            keys.append(i['departmentId'])
            values.append(i['displayName'])

        for j in keys:
            department_dict[j] = values[keys.index(j)]



        if r_status == 200:
            return render(request, 'base.html', {'departments': department_dict})


# def Works(request):
#     r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=1&q=cat')
#     data = r.text
#     parse_json = json.loads(data)
#     parse_json = parse_json['objectIDs']
#
#     new_obj = []
#
#     for i in parse_json:
#         r = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(i))
#         data = r.text
#         parse_json = json.loads(data)
#         new_obj.append(parse_json)
#
#     final_dict = {}
#     for j in range(len(new_obj)):
#         final_dict[new_obj[j]['primaryImage']] = new_obj[j]['artistDisplayName']
#
#
#
#     return render(request, 'arts.html', {'Data': final_dict})