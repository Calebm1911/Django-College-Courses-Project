from django.urls import path
from courses import views

urlpatterns = [
    path('',views.course_view, name='index'),
    path('<int:pk>/', views.course_detail,name='course_detail')
]