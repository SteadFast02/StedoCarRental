from django.shortcuts import render
from rest_framework.decorators import api_view
from CarRentalSystemApp.serializer import VehicleSerializer
from CarRentalSystemApp.models import Vehicle
from . import tuple_to_dict
from django.db import connection
from django.shortcuts import redirect
from django.http.response import JsonResponse

# For showing pade in dashboard 
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
@xframe_options_exempt
@api_view(['GET','POST'])
def VehicleInterface(request):
    return render(request,'VehicleInterface.html')

@xframe_options_exempt
@api_view(['GET','POST'])
def VehicleSubmit(request):
    if request.method == 'POST':
        vehicle_serializer = VehicleSerializer(data=request.data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            return render(request,"VehicleInterface.html",{"pass":"Record Submitted Successfully"})
        return render(request,"VehicleInterface.html",{"fail":"Fail to Submit Record"})

@xframe_options_exempt    
@api_view(['GET','POST'])
def DisplayAllVehicle(request):
  try:
    if request.method == 'GET':
      q = "select V.*,(select C.categoryname from carrentalsystemapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from carrentalsystemapp_subcategory S where S.id=V.subcategoryid) as subcategoryname from carrentalsystemapp_vehicle V"
      # print(q)
      cursor = connection.cursor()
      cursor.execute(q)
      records = tuple_to_dict.ParseDictMultipleRecord(cursor)
      # print("xxxxxxxxxx",records)
    
      return render(request,'VehicleDisplay.html',{'data':records})
  except Exception as e:
       print("Error:",e)
       return render(request,'VehicleDisplay.html',{'data':{}})
 
@xframe_options_exempt   
@api_view(['GET','POST'])
def DisplayById(request):
  try:
    if request.method == 'GET':
      q="select V.*,(select C.categoryname from carrentalsystemapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from carrentalsystemapp_subcategory S where S.id=V.subcategoryid) as subcategoryname from carrentalsystemapp_vehicle V where V.id={0}".format(request.GET['id'])
      cursor=connection.cursor()
      cursor.execute(q)
      record=tuple_to_dict.ParseSingleDict(cursor)
      return render(request,'VehicleById.html',{'data':record})
  except Exception as e:
       print("Error:",e)
       return render(request,'VehicleById.html',{'data':{}})

@xframe_options_exempt     
@api_view(['GET','POST'])
def VehicleUpdate(request):
  try:
    if request.method == 'GET':
      # print('xxxxxxxxxxxxxxx',request.GET['btn'])
      if(request.GET['btn']=="Edit"):
      #  print(request.GET['btn'])
       vehicle=Vehicle.objects.get(pk=request.GET['id'])
       vehicle.categoryid=request.GET['categoryid']
       vehicle.subcategoryid=request.GET['subcategoryid']
       vehicle.modelyear=request.GET['modelyear']
       vehicle.variant=request.GET['variant']
       vehicle.price=request.GET['price']
       vehicle.insured=request.GET['insured']
       vehicle.ownername=request.GET['ownername']
       vehicle.mobileno=request.GET['mobileno']
       vehicle.color=request.GET['color']
       vehicle.fueltype=request.GET['fueltype']
       vehicle.numofseats=request.GET['numofseats']
       vehicle.transmissiontype=request.GET['transmissiontype']      
       vehicle.save()
      else:
        # print("Hello1")
        vehicle=Vehicle.objects.get(pk=request.GET['id']) 
        vehicle.delete() 
      return redirect('/api/displayallvehicle')
  except Exception as e:
       print("Error:",e)
       return redirect('/api/displayallvehicle')

@xframe_options_exempt   
@api_view(['GET','POST'])
def DisplayVehicleIcon(request):
  try:
    if request.method == 'GET':
       return render(request,'VehicleIconDisplay.html',{'data':dict(request.GET)})
  except Exception as e:   
       return render(request,'VehicleIconDisplay.html',{'data':{}})
