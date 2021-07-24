from django.urls import path
from .views.password_change import *
from .views.password_change_done import *
from .views.logout import *

app_name = 'users'
urlpatterns = [
    path('logout', LogoutView.as_view(), name="logout"),
    path('password_change', UserPasswordChangeView.as_view(), name="password_change"),
    path('password_change/done', UserPasswordChangeDoneView.as_view(), name="password_change_done")
]
