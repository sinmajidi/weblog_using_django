from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.aboutpage),
    path('', views.homepage),
    path('articles/',include('articles.urls'))

]
