from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('sobre/', views.sobre, name='sobre'),
    path('curso/', include('curso.urls')),
]