from django.urls import path
from .views import news_list, news_detail , home_page_view , contact_us , about_us , page_404

urlpatterns = [
    path('' , home_page_view, name='home_page_view'),
    path('news/', news_list, name='news_list'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('contact-us/', contact_us, name='contact_us'),
    path('about/', about_us, name='about_us'),
    path('page_404/', page_404, name='page_404'),

]