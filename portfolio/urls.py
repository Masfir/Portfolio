from django.urls import path
from .import views

urlpatterns = [
   
    path('', views.index, name ='index'),
    path('about', views.about, name ='about'),
    path('contact', views.contact, name ='contact'),
    path('contact_details', views.contact_details, name ='contact_details'),
    path('blog', views.handleblog, name='handleblog'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('contact_search', views.contact_search, name='contact_search'),
    path('contact_search_id', views.contact_search_id, name='contact_search_id'),
    path('google_map', views.google_map, name='google_map'),
       

]
