from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add-job/', views.add_job),
    path('jobs/', views.job_list),
    path('delete-job/<int:id>/', views.delete_job),
     path('edit-job/<int:id>/', views.edit_job),
]
