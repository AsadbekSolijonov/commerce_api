from django.urls import path
from store import views
urlpatterns = [
    path('', views.category_list_or_create),
    path('<int:pk>/', views.category_retrieve_update_or_detele)
]
