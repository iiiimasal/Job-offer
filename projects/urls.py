
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
    path('profile/<str:pk>/',views.userProfile,name="user-profile"),
    path('create-company/',views.createCompany,name='create-Company'),
    path('delete-job/<str:pk>/',views.deletecompany,name='delete-company'),
    path('update-job/<str:pk>/',views.updatecompany,name='update-company'),
    path('register-user/',views.create_normal_user,name='user-register'),
    path('register-user/<str:user_id>',views.employer_registration,name='employer-registration'),
    path('register-user/<str:user_id>',views.employee_registration,name='employee-registration'),
    path('delete-message/<str:pk>/',views.deleteMessage,name='delete-message'),
    # path('create-job/', views.create_job, name='create-job'),
    path('create-commercials/', views.createCommercials, name='create-commercials'),
    path('list-commercials/', views.listCommercials, name='list-commercials'),
]
