from django.urls import path
from .import views
from .import Auth
from .import product


urlpatterns = [
  path('dashboard/', views.index, name='dashboard'),

  ###### AUTH 
  path('', Auth.login_form, name="user_login"), 

  ############## PRODUCT
  path('add/product', product.add_product, name="add_product_counter"),
   path('test/product', product.test, name="add_test"),
]