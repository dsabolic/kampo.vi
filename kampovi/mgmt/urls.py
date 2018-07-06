from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('<int:kamp_id>/', views.detail, name="detail"),
	path('<int:kamp_id>/register', views.register, name="register"),
	path('<int:kamp_id>/success', views.success, name="success")
]