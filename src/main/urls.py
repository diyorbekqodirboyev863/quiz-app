# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('quiz/detail/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
	path('test/', views.test, name='test'),
	path('category/detail/<slug:slug>/', views.category_detail, name='category_detail'),
]