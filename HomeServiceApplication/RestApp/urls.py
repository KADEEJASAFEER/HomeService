
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user',UserView.as_view()),
    path('user/<str:pk>',UserDetails.as_view()),
    path('user/addwork/<str:pk>',AddWork.as_view()),
    path('user/username/editwork/<int:pk>',EditWork.as_view())
]
urlpatterns=format_suffix_patterns(urlpatterns)
