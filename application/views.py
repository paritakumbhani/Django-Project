from django.shortcuts import render
from .models import Cheese
from common.common import *
import operator
from functools import *
from django.db.models import Q
import re

def reset(request):
    error = ''
    fdata = getData('canadianCheeseDirectory.csv')
    if(fdata == 'NO_DATA_FOUND'):
        error = fdata
        request.session['data'] = ''
    else:
        Cheese.objects.all().delete()
        dummyData = fdata
        for row in dummyData:
            cheeseModel = Cheese()
            cheeseModel.CheeseId = row[0]
            cheeseModel.CheeseNameEn = row[1]
            cheeseModel.ManufacturerNameEn = row[2]
            cheeseModel.ManufacturerProvCode = row[3]
            cheeseModel.ManufacturingTypeEn = row[4]
            cheeseModel.WebSiteEn = row[5]
            cheeseModel.FatContentPercent = row[6]
            cheeseModel.MoisturePercent = row[7]
            cheeseModel.ParticularitiesEn = row[8]
            cheeseModel.FlavourEn = row[9]
            cheeseModel.CharacteristicsEn = row[10]
            cheeseModel.RipeningEn = row[11]
            cheeseModel.Organic = row[12]
            cheeseModel.CategoryTypeEn = row[13]
            cheeseModel.MilkTypeEn = row[14]
            cheeseModel.MilkTreatmentTypeEn = row[15]
            cheeseModel.RindTypeEn = row[16]
            cheeseModel.LastUpdateDate = row[17]
            cheeseModel.save()
        
        
    dbData = list(Cheese.objects.all().values())
    return render(request, 'application/show.html', {'dbData': dbData, 'columns': Cheese._meta.get_fields(), 'error': error})

def show(request):
    error = ''
    dbData = list(Cheese.objects.all().values())
    if(not(dbData)):
        error = 'NO_DATA_FOUND'
    return render(request, 'application/show.html', {'dbData': dbData, 'columns': Cheese._meta.get_fields(), 'error': error})


def addNew(request):
    if(request.POST):
        new = dict()
        for x in request.POST.keys():
            if(x != 'csrfmiddlewaretoken'):
                new[x] = request.POST[x]
        cheeseModel = Cheese(**new)
        cheeseModel.save()
        dbData = list(Cheese.objects.all().values())
        
        return render(request, 'application/show.html', {'dbData': dbData, 'columns': Cheese._meta.get_fields(), 'error': ''})
    else:
        return render(request, 'application/addnew.html')


def delete(request):
    if(request.POST):
        index = int(request.POST['index'])
        Cheese.objects.filter(id=index).delete()
        dbData = list(Cheese.objects.all().values())
        return render(request, 'application/delete.html', {'dbData': dbData, 'columns': Cheese._meta.get_fields(), 'error': ''})
    else:
        dbData = list(Cheese.objects.all().values())
        if(not(dbData)):
            error = 'NO_DATA_FOUND'
        return render(request, 'application/delete.html', {'dbData': dbData, 'columns': Cheese._meta.get_fields(), 'error': ''})


def update(request):
    if(request.POST):
        index = int(request.POST['index'])
        dbData = list(Cheese.objects.filter(id=index).values())
        return render(request, 'application/editpage.html', {'dbData': dbData, 'columns': Cheese._meta.get_fields(), 'error': '', 'index': index})
    else:
        dbData = list(Cheese.objects.all().values())
        return render(request, 'application/update.html', {'dbData': dbData, 'columns': Cheese._meta.get_fields(),  'error': ''})


def editpage(request):
    if(request.POST):
        print("hi")
        index = int(request.POST['index'])
        updates = dict()
        for x in request.POST.keys():
            if(x != 'csrfmiddlewaretoken' and x!='index'):
                updates[x] = request.POST[x]
        Cheese.objects.filter(id=index).update(**updates)
        
        dbData = list(Cheese.objects.all().values())
        return render(request, 'application/show.html', {'dbData': dbData, 'columns': Cheese._meta.get_fields(),  'error': ''})

    else:
        dbData = list(Cheese.objects.all().values())
        return render(request, 'application/update.html', {'dbData': dbData, 'columns': Cheese._meta.get_fields(),  'error': ''})


def userFilter(request):
    if(request.POST):
        usersFilters = dict()
        for x in request.POST:
            if(re.search("filter_\d",x)):
                filterNumber = x.split('_')
                value = 'value_'+filterNumber[1]
                if(request.POST[value]!=''):
                    usersFilters[request.POST[x]] = request.POST[value]
        error = ""
        dbData = list(Cheese.objects.all().values())
        if(len(usersFilters.keys())>0):
            qList = [Q(**{key: val}) for key, val in usersFilters.items() if key!=""]
            dbData = list(Cheese.objects.filter(reduce(operator.and_,qList)).values())
        else:
            dbData = Cheese.objects.all().values()
            error = "No Filters Applied (Please Select Filters)"   

        if(not(dbData)):
            error = 'NO_DATA_FOUND'

        return render(request, 'application/show.html', {'dbData': dbData, 'columns': Cheese._meta.get_fields(), 'error': error})
    else:
        error =""
        columns = Cheese._meta.get_fields()
        return render(request, 'application/filters.html', { 'error': error,'columns': columns} )