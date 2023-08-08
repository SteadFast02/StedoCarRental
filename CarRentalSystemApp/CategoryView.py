from django.shortcuts import render
from rest_framework.decorators import api_view
from CarRentalSystemApp.serializer import CategorySerializer
from CarRentalSystemApp.models import Category
from . import tuple_to_dict
from django.db import connection
from django.shortcuts import redirect
from django.http.response import JsonResponse
import os

# For showing pade in dashboard 
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.
@xframe_options_exempt
@api_view(['GET','POST'])
def CategoryInterface(request):
    return render(request,'CategoryInterface.html')

@xframe_options_exempt
@api_view(['GET','POST'])
def CategorySubmit(request):
    if request.method == 'POST':
        category_serializer = CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return render(request,"CategoryInterface.html",{"pass":"Record Submitted Successfully"})
        return render(request,"CategoryInterface.html",{"fail":"Fail to Submit Record"})

@xframe_options_exempt    
@api_view(['GET','POST'])
def DisplayAllCategory(request):
  try:
    if request.method == 'GET':
      list_category=Category.objects.all()
      list_category_serializer=CategorySerializer(list_category,many=True)
      records=tuple_to_dict.ParseDict(list_category_serializer.data)
    
      return render(request,'CategoryDisplay.html',{'data':records})
  except Exception as e:
       print("Error:",e)
       return render(request,'CategoryDisplay.html',{'data':{}})


@xframe_options_exempt   
@api_view(['GET','POST'])
def DisplayById(request):
  try:
    if request.method == 'GET':
      q="SELECT * FROM carrentalsystemapp_category where id={0}".format(request.GET['id'])
      cursor=connection.cursor()
      cursor.execute(q)
      record=tuple_to_dict.ParseSingleDict(cursor)
      # print("''''''''",description.cursor)
      return render(request,'CategoryById.html',{'data':record})
  except Exception as e:
       print("Error:",e)
       return render(request,'CategoryById.html',{'data':{}})

@xframe_options_exempt   
@api_view(['GET','POST'])
def CategoryUpdate(request):
  try:
    if request.method == 'GET':
      # print('xxxxxxxxxxxxxxx',request.GET['btn'])
      if(request.GET['btn']=="Edit"):
      #  print(request.GET['btn'])
       category=Category.objects.get(pk=request.GET['id'])
       category.categoryname=request.GET['categoryname']
       category.description=request.GET['description']
       category.save()
      else:
        # print("Hello1")
        category=Category.objects.get(pk=request.GET['id']) 
        category.delete() 
      return redirect('/api/displayallcategory')
  except Exception as e:
       print("Error:",e)
       return redirect('/api/displayallcategory')
     
@xframe_options_exempt     
@api_view(['GET','POST'])
def DisplayCategoryIcon(request):
  try:
    if request.method == 'GET':
       return render(request,'CategoryIconDisplay.html',{'data':dict(request.GET)})
  except Exception as e:   
       return render(request,'CategoryIconDisplay.html',{'data':{}})

@xframe_options_exempt     
@api_view(['GET','POST'])
def Category_Save_Icon(request):
  try:
    if request.method == 'POST':
      
       category=Category.objects.get(pk=request.POST['id'])
       category.icon=request.FILES['icon']
       category.save()
       os.remove('E:/python django project/CarRentalSystem'+request.POST['oldpic'])
       return redirect('/api/displayallcategory')
  except Exception as e:
     print("Error:",e)
     return redirect('/api/displayallcategory')    

@xframe_options_exempt
@api_view(['GET','POST'])
def JsonCategory(request):
  try:
    if request.method == 'GET':
      list_category=Category.objects.all()
      list_category_serializer=CategorySerializer(list_category,many=True)
      records=tuple_to_dict.ParseDict(list_category_serializer.data)
    
      return JsonResponse(records,safe=False)
  except Exception as e:
       print("Error:",e)
       return JsonResponse([],safe=False)
