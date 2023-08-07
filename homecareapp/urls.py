
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about.html', views.about, name="about"),
    path('services.html', views.services, name="services"),
    path('blog.html', views.blog, name="blog"),
    path('blog-single.html', views.blogsingle, name="blog-single"),
    path('contact.html', views.contact, name="contact"),
]
