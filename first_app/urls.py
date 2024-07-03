from django.urls import path
from . import views
urlpatterns = [
     path('',views.home,name='homepage'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('pass_change/',views.pass_change,name='passchange'),
    path('profile/',views.profile,name='profile'),

]