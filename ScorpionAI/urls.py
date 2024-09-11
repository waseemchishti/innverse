"""
URL configuration for ScorpionAI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from ScorpionAI import views
from . import settings
from django.conf.urls.static import static

admin.site.site_header = "Innverse Solution Admin"
admin.site.site_title = "Innverse Solution Admin Portal"
admin.site.index_title = "Welcome to Innverse Solution Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about-us/', views.about),
    path('career/', views.career),
    path('blog/', views.blog, name="blog"),
    path('blog_category/<int:pk>', views.blog_category, name='blog_category'),
    path('news/', views.news),
    path('contact/', views.contact, name="contactform"),
    path('retail/', views.retail),
    path('fintech/', views.fintech),
    path('health-care/', views.health),
    path('waste-management/', views.waste),
    path('real-estate/', views.real),
    path('ecommerce/', views.ecommerce),
    path('customize-AI-solution/', views.customizeAI),
    path('generative-AI/', views.generative),
    path('natural-langauge-processing/', views.nlp),
    path('data-science/', views.dataScience),
    path('computer-vision/', views.computerVision),
    path('big-data-analytics/', views.bigData),
    path('data-engineering/', views.dataEngineering),
    path('AI-strategy-concultation/', views.aiStrategy),
    path('website-development/', views.webDevelopment),
    path('mobile-app-development/', views.appDevelopment),
    path('secrch-engine-optimization/', views.seo),
    path('digital-marketing/', views.digitalMarketing),
    path('life-at-innverse/', views.life)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
