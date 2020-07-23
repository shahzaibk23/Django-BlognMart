from django.urls import path

from .views import sellerDetailsPage


app_name = "Seller"
urlpatterns = [
    path('<int:seller_id>/', sellerDetailsPage, name="seller_details"),

]