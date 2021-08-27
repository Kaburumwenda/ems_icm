from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout), 
    path('orders/', views.OrdersList.as_view()),   
    path('order/<int:id>', views.OrdersItem.as_view()), 
    path('latest/order/', views.LatestOrder.as_view()),  
]