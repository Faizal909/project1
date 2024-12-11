from django.urls import path
from.import views
urlpatterns=[path("", views.home, name="home"),
             path("path1", views.form, name="form"),
             path("path2", views.login, name="login"),
             path("path3", views.data, name="data"),
             path("path4",views.new_login,name="new_login"),]