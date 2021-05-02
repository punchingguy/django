from django.urls import path
from . import views

urlpatterns = [
    path("test", views.test, name="test"),
    path("login",views.login, name="login"),
    path("logout",views.logout, name="logout"),
    path("register",views.register, name="register"),
    path("resume",views.resume, name="resume"),
    # path("check_resume", views.check_resume, "check_resume"),
]