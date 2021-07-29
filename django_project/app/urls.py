from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('listTrend/',views.Trend),
    path('listCorona/',views.Corona),
    path('listGame/',views.Game),

]
