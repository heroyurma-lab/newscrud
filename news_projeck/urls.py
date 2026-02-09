from django.urls import path
from .views import news_list, news_detail , home_page_view , contact_us , about_us , page_404 , EditView, DeleteView, CreateView

urlpatterns = [
    path('' , home_page_view, name='home_page_view'),
    path('news/', news_list, name='news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail'),
    path('news/<slug>/edit/', EditView.as_view() , name='news_edit'),
    path('news/<slug>/delete/', DeleteView.as_view(), name='news_delete'),
    path('create/', CreateView.as_view(), name='news_create'),
    path('contact-us/', contact_us, name='contact_us'),
    path('about-us/', about_us, name='about_us'),
    path('page-404/', page_404, name='page_404'),
]