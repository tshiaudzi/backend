# from unicodedata import name
from django.urls import path
from .views import Myview
from.views import book_list,Post_list,post_detail,loginView,profileView,logout_View

app_name='blog'

urlpatterns = [
    path("book_list/", book_list),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name="post_detail"),
    path("",Post_list,name="home"),
    path('login/',loginView, name="login"),
    path("profile/",profileView,name="profile"),
    path("logout/",logout_View,name="logout")
]

