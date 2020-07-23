from django.urls import path

from .views import create_view, single_blog_view, blog_view, comment_view, category_view
from django.conf import settings
from django.conf.urls.static import static


app_name = "Blog"

urlpatterns = [
    path('create/', create_view, name="create"),
    path('<int:my_id>/', single_blog_view, name='blogDetails'),
    path('<int:my_id>/comment/',comment_view, name= "comment"),
    path('category/<int:cat_id>/',category_view, name= "category")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)