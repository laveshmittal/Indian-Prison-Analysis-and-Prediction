from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [path("a", views.app1homepage),
               path('', views.loginview),
               path("func1", views.func1),
               path("statecount", views.statecount),
               path("educationcount", views.educationcount),
               path("educationcountfunc", views.educationcountfunc),
               path("dashboard", views.dashboard),
               path("escapescount", views.escapescount),
               path("escapescountfunc", views.escapescountfunc),
               path('sentenceperiod', views.sentenceperiod),
               path("sentencefunc", views.sentecefunc),
               path("onlystate", views.onlystate),
               path("onlyyear", views.onlyyear),
               path("predictfunc", views.predictfunc),
               path('admin/', admin.site.urls),
               path("predictcount", views.predictcount)


               ]
