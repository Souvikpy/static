from django.urls import path
from myapp02 import views
app_name="myapp02"

urlpatterns = [
    path('trial/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
]