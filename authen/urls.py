from django.urls import path
from . import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('register/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('update_profile/',views.updateProfile,name='updateProfile'),
    path('update_pass/',views.updatePass,name='updatePass'),
    path('signout/',views.signout,name='signout')
]