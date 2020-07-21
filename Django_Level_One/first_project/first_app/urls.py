from django.conf.urls import url
from Django_Level_One.first_project.first_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
