"""CarRentalSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from CarRentalSystemApp import CategoryView
from CarRentalSystemApp import SubCategoryView
from CarRentalSystemApp import VehicleView
from CarRentalSystemApp import AdminLogin
from CarRentalSystemApp import UserView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    url(r'^api/categoryinterface', CategoryView.CategoryInterface), 
    url(r'^api/submitcategory', CategoryView.CategorySubmit), 
    url(r'^api/displayallcategory', CategoryView.DisplayAllCategory), 
    url(r'^api/displaycategorybyid', CategoryView.DisplayById), 
    url(r'^api/updatecategory', CategoryView.CategoryUpdate), 
    url(r'^api/displaycategoryicon', CategoryView.DisplayCategoryIcon), 
    url(r'^api/cat_save_icon', CategoryView.Category_Save_Icon), 
    url(r'^api/jsoncategory', CategoryView.JsonCategory), 
    

    url(r'^api/subcategoryinterface', SubCategoryView.SubCategoryInterface), 
    url(r'^api/submitsubcategory', SubCategoryView.SubCategorySubmit), 
    url(r'^api/displayallsubcategory', SubCategoryView.DisplayAllSubCategory), 
    url(r'^api/displaysubcategorybyid', SubCategoryView.DisplayById), 
    url(r'^api/updatesubcategory', SubCategoryView.SubCategoryUpdate), 
    url(r'^api/displaysubcategoryicon', SubCategoryView.DisplaySubCategoryIcon), 
    url(r'^api/subcat_save_icon', SubCategoryView.SubCategoryUpdateIcon),
    url(r'^api/jsondisplaysubcategorybyid', SubCategoryView.JsonDisplaySubcategoryById), 
    
    url(r'^api/vehicleinterface', VehicleView.VehicleInterface), 
    url(r'^api/vehiclesubmit', VehicleView.VehicleSubmit), 
    url(r'^api/displayallvehicle', VehicleView.DisplayAllVehicle), 
    url(r'^api/displayvehiclebyid', VehicleView.DisplayById), 
    
    url(r'^api/displayvehicleicon', VehicleView.DisplayVehicleIcon), 
    
    
    url(r'^api/adminlogininterface', AdminLogin.AdminLoginInterface), 
    url(r'^api/checkadminlogin',AdminLogin.CheckAdminLogin), 
    
    url(r'^api/admindashboardinterface', AdminLogin.AdminDashBoardInterface), 
    
    url(r'^api/indexinterface', UserView.IndexPage), 
    
    url(r'^api/home',UserView.Home), 
    url(r'^api/showvehiclelist',UserView.ShowVehicleList), 
    url(r'^api/displayselectedvehicle',UserView.DisplaySelectedVehicle), 
    url(r'^api/displayvehicleinhomepage',UserView.DisplayVehicleInHomePage), 
    url(r'^api/faqs',UserView.Faqs), 
    
    url(r'^api/fetchallcategory',UserView.FetchAllCategory), 
    url(r'^api/fetchallbrand',UserView.FetchAllBrand), 
    url(r'^api/fetchallsubcategory',UserView.FetchAllSubcategory), 
    url(r'^api/fetchvehiclecount',UserView.FetchVehicleCount), 
    url(r'^api/setemailmobile',UserView.SetMobileAndEmail), 
    
    
    
    
]
