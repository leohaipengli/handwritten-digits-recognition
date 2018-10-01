from django.urls import path # django 2.0

from . import views

app_name = 'handwritten_digits'
urlpatterns = [
    path('', views.index, name='index'),
    path('recognize/', views.recognize, name='recognize')
]