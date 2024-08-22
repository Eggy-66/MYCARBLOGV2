from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/add/', views.add_item, name='add_item'),
    path('item/<int:pk>/update/', views.item_update, name='item_update'),
    path('item/<int:pk>/delete/', views.item_confirm_delete, name='item_confirm_delete'),
    path('item/<int:item_id>/message/', views.send_message, name='send_message'),
]
