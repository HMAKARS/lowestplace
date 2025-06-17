from django.urls import path
from . import views

app_name = 'templates_app'

urlpatterns = [
    path('', views.home, name='home'),
    # 스타트업 템플릿
    path('startup/', views.startup_landing, name='startup_landing'),
    # 상품소개 템플릿
    path('product/', views.product_landing, name='product_landing'),
    # 음식점 템플릿
    path('restaurant/', views.restaurant_landing, name='restaurant_landing'),
    # 교회/성당 템플릿 - 전체 사이트
    path('traditional/', views.traditional_template, name='traditional'),
    path('modern/', views.modern_template, name='modern'),
    # 교회/성당 템플릿 - 랜딩페이지
    path('landing-modern/', views.modern_landing, name='modern_landing'),
    path('landing-traditional/', views.traditional_landing, name='traditional_landing'),
]
