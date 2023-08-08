from django.shortcuts import render
from rest_framework.decorators import api_view
from CarRentalSystemApp.serializer import AdminSerializer
from CarRentalSystemApp.models import Admin
from . import tuple_to_dict
from django.db import connection
from django.shortcuts import redirect
from django.http.response import JsonResponse

# Create your views here.
@api_view(['GET','POST'])
def AdminLoginInterface(request):
    return render(request,'AdminLogin.html',)

@api_view(['GET','POST'])
def CheckAdminLogin(request):
    try:
        if request.method == 'GET':
            # print("ONE")
            q = "select * from carrentalsystemapp_admin  where (mobileno='{0}' or emailid='{0}') and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
            # print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            # print("Check",len(record))
            if(len(record)==0):
                return render(request,"AdminLogin.html",{'fail':"Inavlid Adminid/Password"})
            else:
               
               return render(request,"AdminDashBoard.html",{'data':record[0],'pass':'Login Successfully'})
            
            
    except Exception as e:
        print("Error : ",e)
        return render(request,"AdminDashBoard.html",{'data':[]})

@api_view(['GET','POST'])
def AdminDashBoardInterface(request):
    return render(request,'AdminDashBoard.html')