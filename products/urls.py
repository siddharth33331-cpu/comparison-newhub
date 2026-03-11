from django.urls import path
from . import views

urlpatterns = [

    path('', views.product_list, name='product_list'),

    path('category/<str:category_name>/', views.category_page, name='category_page'),

    path('compare/', views.compare_products, name='compare_products'),

    path('forum/', views.forum_home, name='forum_home'),

    path('forum/thread/<int:thread_id>/', views.thread_page, name='thread_page'),

]