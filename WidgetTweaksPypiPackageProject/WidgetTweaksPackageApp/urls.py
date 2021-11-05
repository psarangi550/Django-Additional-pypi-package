from django.urls import path
from WidgetTweaksPackageApp import views

app_name="tweak"

urlpatterns = [
    path('', views.index_view)
]
