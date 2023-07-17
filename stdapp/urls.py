from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('coursedetails',views.coursedetails,name='coursedetails'),
    path('studadd',views.studadd,name='studadd'),
    path('showstudent',views.showstudent,name='showstudent'),
    path('add_coursedb',views.add_coursedb,name="add_coursedb"),
    path('add_studentdb',views.add_studentdb,name="add_studentdb"),
    path('showstudent',views.showstudent,name='showstudent'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editdb/<int:pk>',views.editdb,name='editdb'),
    path('delete/<int:pk>',views.delete,name='delete'),
]