from django.contrib.auth import views as auth_views
from django.conf.urls import url
from accountss import views
app_name = 'accountss'
urlpatterns = [
    url(r'login/',auth_views.LoginView.as_view(template_name='accountss/login.html'),name='login'),
    url(r'logout/',auth_views.LogoutView.as_view(),name='logout'),
    url(r'signup',views.SignUp.as_view(),name='signup') 
]