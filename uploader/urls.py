from django.urls import path
from . import views

urlpatterns = [
    path('uploader/',views.UploaderView.as_view({"post":"create"}),name='uploaderview'),

]