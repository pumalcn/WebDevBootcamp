from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('school/', views.SchoolListView.as_view(), name='list'),
    path('school/<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('school/create/', views.SchoolCreateView.as_view(), name='create'),
    path('school/update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('school/delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete')
]
