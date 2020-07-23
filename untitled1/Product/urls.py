from django.urls import path

from .views import create_view, comment_view, addToCartView, category_view
from pages.views import single_list_view


app_name = "Product"
urlpatterns = [
    path('create/',create_view, name="product_create"),
    path('<int:my_id>/', single_list_view, name = "prod_details"),
    path('<int:my_id>/comment/',comment_view, name="comment" ),
    path('<int:my_id>/add-to-cart/',addToCartView, name="add_to_cart" ),
    path("category/<int:cat_id>/", category_view, name='category')
]