from django.urls import include, path
from .views import MountainPeakList, MountainPeakCreate, MountainPeakDelete, MountainPeakUpdate, MountainPeakDetail 


urlpatterns = [
    path('create/', MountainPeakCreate.as_view(), name='create-mountain-peak'),
    path('', MountainPeakList.as_view()),
    path('<int:pk>/', MountainPeakDetail.as_view(), name='retrieve-mountain-peak'),
    path('update/<int:pk>/', MountainPeakUpdate.as_view(), name='update-mountain-peak'),
    path('delete/<int:pk>/', MountainPeakDelete.as_view(), name='delete-mountain-peak')
]