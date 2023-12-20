from django.urls import path
from knox import views as knox_views

from app.views import CreateUserView, LoginView, ManageUserView

urlpatterns = [
    
    path('create/', CreateUserView.as_view(), name="create"),
     path('profile/', ManageUserView.as_view(), name='profile'),
     path(r'login/', LoginView.as_view(), name='knox_login'),
     path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
     path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]