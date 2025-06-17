from django.urls import path
from . import views

app_name = 'templates_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('traditional/', views.traditional_template, name='traditional'),
    path('modern/', views.modern_template, name='modern'),
    path('landing-modern/', views.modern_landing, name='modern_landing'),
    path('landing-traditional/', views.traditional_landing, name='traditional_landing'),
]
