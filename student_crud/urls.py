from django.urls import path
from .import views

urlpatterns = [
    path('',views.student,name='student'),
    path('student_list',views.student_list,name='student_list'),
    path('student_form',views.student_form,name='student_form'),
    path('<int:id>/',views.student_form,name='student_update'),
    path('delete/<int:id>/',views.delete,name='delete'),


]
