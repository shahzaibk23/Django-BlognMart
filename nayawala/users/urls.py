from django.urls import path
from .views import  signupPage,loginPage

App_name= "user"

urlpatterns = [
    path("signup/", signupPage, name="signup"),
    path("login/", loginPage, name="login"),

]
