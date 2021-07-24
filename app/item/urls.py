from django.urls import path
from .views.item_register import * 

app_name = 'item'
urlpatterns = [
    path('register', ItemRegisterView.as_view(), name="register"),
]
