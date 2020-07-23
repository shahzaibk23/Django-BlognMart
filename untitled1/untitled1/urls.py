"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home_view,contact_view,  single_blog_view, about_view, product_list_view, single_list_view,  checkout_view, cart_view, confirmation_view, elements_view
from Product.views import create_view
from users.views import signup_view, login_view
from Blog.views import blog_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='index'),
    path('about/', about_view, name='about'),
    path('blog/',blog_view, name='blog'),

    path('login/', login_view, name='login'),
    path('login/', login_view, name='single-product'),
    path('checkout/', checkout_view, name='checkout'),
    path('cart/', cart_view, name='cart'),
    path('confirmation/',confirmation_view, name='confirmation' ),
    path('elements/', elements_view, name='elements'),
    path('single-blog/', single_blog_view, name='single-blog'),
    path('contact/', contact_view, name='contact'),
    path('product-list/', product_list_view, name='product_list'),
    path('product/', include('Product.urls')),
    # path('product/create/', create_view, name='p_create')
    path('signup/', signup_view, name='signup'),
    path('seller/', include('seller.urls')),
    path('blog/', include("Blog.urls"))

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
