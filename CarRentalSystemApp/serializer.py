from rest_framework import serializers

from CarRentalSystemApp.models import Category
from CarRentalSystemApp.models import SubCategory
from CarRentalSystemApp.models import Vehicle
from CarRentalSystemApp.models import Admin


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ('id','categoryname','description','icon')


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields = ('id','categoryid','companyname','subcategoryname','subcategorydescription','subcategoryicon')
        
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields = ('id','categoryid','subcategoryid','modelyear','variant','price','insured','registrationno','ownername','mobileno','color','fueltype','numofseats','transmissiontype','vehicleicon')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields = ('id','adminname','mobileno','emailid','password','adminpic')