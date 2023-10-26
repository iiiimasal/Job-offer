
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('admin/', admin.site.urls),
    path('',views.home,name='home-page'),
    path('Jobs/<str:pk>',views.Jobs,name='jobs'),
    path('company/<str:pk>',views.company,name='companies'),
    path('create-company/',views.createCompany,name='create-Company'),
    path('delete-job/<str:pk>/',views.deletecompany,name='delete-company'),
    path('update-job/<str:pk>/',views.updatecompany,name='update-company'),
    path('register-employee/',views.employee_registration,name='employee-register'),
]
