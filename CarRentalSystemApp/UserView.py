from django.shortcuts import render
from rest_framework.decorators import api_view
from CarRentalSystemApp.serializer import CategorySerializer
from CarRentalSystemApp.models import Category
from . import tuple_to_dict
from django.db import connection
from django.shortcuts import redirect
from django.http.response import JsonResponse
import os
import json
import datetime

@api_view(['GET','POST'])
def IndexPage(request):
    return render(request,'Index.html')

@api_view(['GET','POST','DELETE'])
def ShowVehicleList(request):
#    print("11",request.GET['dh'])
   userdata={'mobileno':'','city':request.GET['city'],'starttime':request.GET['starttime'],'endtime':request.GET['endtime'],'days':request.GET['dh']}
   request.session["USERDATA"]=userdata
   return JsonResponse(userdata,safe=False)

@api_view(['GET','POST','DELETE'])
def SetMobileAndEmail(request):
  
   userdata=request.session["USERDATA"]
   userdata['mobileno']=request.GET['mobileno']
   userdata['emailaddress']=request.GET['emailaddress']
   userdata['amount']=request.GET['amount']
   request.session["USERDATA"]=userdata
   return JsonResponse(userdata,safe=False)

@api_view(['GET','POST','DELETE'])
def Home(request):
    userdata=request.session["USERDATA"]
    # print("UUUUUSSSSEEER",userdata)
    return render(request,"Home.html",{'userdata':userdata})  

@api_view(['GET','POST','DELETE'])
def DisplaySelectedVehicle(request):
    vehicle=request.GET['vehicle']
    selected_vehicle=json.loads(vehicle)
    userdata=request.session["USERDATA"]
    st=datetime.datetime.strptime(userdata['starttime'],"%Y/%m/%d %H:%M")
    et=datetime.datetime.strptime(userdata['endtime'],"%Y/%m/%d %H:%M")
    userdata['starttime']=datetime.datetime.strftime(st,"%a,%d %b %Y")
    userdata['endtime']=datetime.datetime.strftime(et,"%a,%d %b %Y")
    d=userdata['days'].split(":")
    userdata['days']=d[0]+" Days"+" "+d[1]+" Hours"
    userdata['fare']=selected_vehicle['price']
    hr=int(selected_vehicle['price'])//24
    userdata['amount']=int(d[0])*int(selected_vehicle['price'])+(hr*int(d[1]))
    userdata['netamount']=userdata['amount']+400
    return render(request,"DisplaySelectedVehicle.html",{'vehicle':selected_vehicle,'userdata':userdata})

@api_view(['GET','POST','DELETE'])
def Faqs(request):
    return render(request,"faqs.html")

@api_view(['GET','POST','DELETE'])
def DisplayVehicleInHomePage(request):
    try:
        if request.method == 'GET':
            if(request.GET['param']=="all"):
                q = "select V.*,(select C.categoryname from carrentalsystemapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from carrentalsystemapp_subcategory S where S.id=V.subcategoryid) as subcategoryname,(select S.companyname from carrentalsystemapp_subcategory S where S.id=V.subcategoryid) as companyname from carrentalsystemapp_vehicle V"
            else:
                q = "select V.*,(select C.categoryname from carrentalsystemapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from carrentalsystemapp_subcategory S where S.id=V.subcategoryid) as subcategoryname,(select S.companyname from carrentalsystemapp_subcategory S where S.id=V.subcategoryid) as companyname from carrentalsystemapp_vehicle V where V.subcategoryid in(select id from carrentalsystemapp_subcategory where companyname in ({}))".format(request.GET['param']) 
            # Optimize 
            # q="SELECT V.*, C.categoryname, S.subcategoryname, S.companyname FROM carrentalsystemapp_vehicle V JOIN carrentalsystemapp_category C ON C.id = V.categoryid JOIN carrentalsystemapp_subcategory S ON S.id = V.subcategoryid;"
            # print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            # print("xxxxxxxxxx",records)
            return JsonResponse(records,safe=False)
    except Exception as e:
        print("Error : " ,e)
        return JsonResponse(records,safe=False)

@api_view(['GET','POST','DELETE'])
def FetchVehicleCount(request):
    try:
        if request.method == 'GET':
            q = "SELECT COUNT(*) as C FROM carrentalsystem.carrentalsystemapp_vehicle;"
            # print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            # print("xxxxxxxxxx",records)
            return JsonResponse(records,safe=False)
    except Exception as e:
        print("Error : " ,e)
        return JsonResponse(records,safe=False)


@api_view(['GET','POST','DELETE'])
def FetchAllCategory(request):
    try:
        if request.method == 'GET':
            q = "SELECT * from carrentalsystemapp_category"
            # print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            # print("xxxxxxxxxx",records)
            return JsonResponse(records,safe=False)
    except Exception as e:
        print("Error : " ,e)
        return JsonResponse(records,safe=False)
    
@api_view(['GET','POST','DELETE'])
def FetchAllBrand(request):
    try:
        if request.method == 'GET':
            q = "SELECT * FROM carrentalsystemapp_subcategory group by companyname;"
            # print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            # print("xxxxxxxxxx",records)
            return JsonResponse(records,safe=False)
    except Exception as e:
        print("Error : " ,e)
        return JsonResponse(records,safe=False)
    
@api_view(['GET','POST','DELETE'])
def FetchAllSubcategory(request):
    try:
        if request.method == 'GET':
            q = "SELECT * FROM carrentalsystemapp_subcategory group by subcategoryname;"
            # print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            # print("xxxxxxxxxx",records)
            return JsonResponse(records,safe=False)
    except Exception as e:
        print("Error : " ,e)
        return JsonResponse(records,safe=False)