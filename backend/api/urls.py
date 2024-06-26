from django.urls import path
from . import views


# Define the URL patterns for the API endpoints
urlpatterns = [
    path('api/get_data/', views.get_data, name='get_data'),
    path('api/name_search/', views.name_search, name='name_search'),
    path('api/save_search/', views.save_search, name='save_search'),
    path('api/search_history/', views.get_search_history, name='get_search_history'),
    path('api/prescriptions/', views.PrescriptionListCreateView.as_view(), name='prescriptions'),
    path('api/prescriptions/<str:rxid>/', views.PrescriptionDeleteView.as_view(), name='delete_prescription'),
]