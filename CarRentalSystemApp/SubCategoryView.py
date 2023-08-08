from django.shortcuts import render
from rest_framework.decorators import api_view
from CarRentalSystemApp.serializer import SubCategorySerializer
from CarRentalSystemApp.models import SubCategory
from . import tuple_to_dict
from django.db import connection
from django.shortcuts import redirect
from django.http.response import JsonResponse

# For showing pade in dashboard 
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.
@xframe_options_exempt
@api_view(['GET','POST'])
def SubCategoryInterface(request):
    return render(request,'SubCategoryInterface.html')

@xframe_options_exempt
@api_view(['GET','POST'])
def SubCategorySubmit(request):
    if request.method == 'POST':
        subcategory_serializer = SubCategorySerializer(data=request.data)
        if subcategory_serializer.is_valid():
            subcategory_serializer.save()
            return render(request,"SubCategoryInterface.html",{"pass":"Record Submitted Successfully"})
        return render(request,"SubCategoryInterface.html",{"fail":"Fail to Submit Record"})

'''
@xframe_options_exempt    
@api_view(['GET','POST'])
def DisplayAllSubCategory(request):
  try:
    if request.method == 'GET':
      list_subcategory=SubCategory.objects.all()
      list_subcategory_serializer=SubCategorySerializer(list_subcategory,many=True)
      records=tuple_to_dict.ParseDict(list_subcategory_serializer.data)
    
      return render(request,'SubCategoryDisplay.html',{'data':records})
  except Exception as e:
       print("Error:",e)
       return render(request,'SubCategoryDisplay.html',{'data':{}})
'''

@xframe_options_exempt    
@api_view(['GET','POST'])
def DisplayAllSubCategory(request):
  try:
    if request.method == 'GET':
      q = "select S.*,(select C.categoryname from carrentalsystemapp_category C where C.id=S.categoryid) as categoryname from carrentalsystemapp_subcategory S"
      # print(q)
      cursor = connection.cursor()
      cursor.execute(q)
      records = tuple_to_dict.ParseDictMultipleRecord(cursor)
      # print("xxxxxxxxxx",records)
    
      return render(request,'SubCategoryDisplay.html',{'data':records})
  except Exception as e:
       print("Error:",e)
       return render(request,'SubCategoryDisplay.html',{'data':{}})

@xframe_options_exempt   
@api_view(['GET','POST'])
def DisplayById(request):
  try:
    if request.method == 'GET':
      q="select S.*,(select C.categoryname from carrentalsystemapp_category C where C.id=S.categoryid) as categoryname from carrentalsystemapp_subcategory S where id={0}".format(request.GET['id'])
      cursor=connection.cursor()
      cursor.execute(q)
      record=tuple_to_dict.ParseSingleDict(cursor)
      # print("''''''''",description.cursor)
      return render(request,'SubCategoryById.html',{'data':record})
  except Exception as e:
       print("Error:",e)
       return render(request,'SubCategoryById.html',{'data':{}})

@xframe_options_exempt   
@api_view(['GET','POST'])
def SubCategoryUpdate(request):
  try:
    if request.method == 'GET':
      # print('xxxxxxxxxxxxxxx',request.GET['btn'])
      if(request.GET['btn']=="Edit"):
      #  print(request.GET['btn'])
       subcategory=SubCategory.objects.get(pk=request.GET['id'])
       subcategory.categoryid=request.GET['categoryid']
       subcategory.companyname=request.GET['companyname']
       subcategory.subcategoryname=request.GET['subcategoryname']
       subcategory.subcategorydescription=request.GET['subcategorydescription']
       subcategory.save()
      else:
        # print("Hello1")
        subcategory=SubCategory.objects.get(pk=request.GET['id']) 
        subcategory.delete() 
      return redirect('/api/displayallsubcategory')
  except Exception as e:
       print("Error:",e)
       return redirect('/api/displayallsubcategory')

@xframe_options_exempt   
@api_view(['GET','POST'])
def DisplaySubCategoryIcon(request):
  try:
    if request.method == 'GET':
       return render(request,'SubCategoryIconDisplay.html',{'data':dict(request.GET)})
  except Exception as e:   
       return render(request,'SubCategoryIconDisplay.html',{'data':{}})

@xframe_options_exempt     
@api_view(['GET','POST'])
def SubCategoryUpdateIcon(request):
  try:
    if request.method == 'POST':
      
       subcategory=SubCategory.objects.get(pk=request.POST['id'])
       subcategory.subcategoryicon=request.FILES['subcategoryicon']
       subcategory.save()
       return redirect('/api/displayallsubcategory')
  except Exception as e:
     print("Error:",e)
     return redirect('/api/displayallsubcategory')
   
@xframe_options_exempt   
@api_view(['GET','POST'])
def JsonDisplaySubcategoryById(request):
  try:
    if request.method == 'GET':
      q="SELECT * FROM carrentalsystem.carrentalsystemapp_subcategory where categoryid={0};".format(request.GET['cid'])
      cursor=connection.cursor()
      cursor.execute(q)
      record=tuple_to_dict.ParseDictMultipleRecord(cursor)
      # print("''''''''",description.cursor)
      return JsonResponse(record,safe=False)

  except Exception as e:
       print("Error:",e)
       return JsonResponse([],safe=False)
