# from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Myview
from.views import book_list,Post_list,post_detail

app_name='blog'

urlpatterns = [
    path("book_list/", book_list),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name="post_detail"),
    path("",Post_list,name="home")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)