from django.conf.urls import url
from Django_Level_One.ProTwo.appTwo import views

urlpatterns = [
    url(r'^$',views.help,name='help'),
]
