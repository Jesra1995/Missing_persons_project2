from django.urls import path, include
from .views import homeView, tableView

urlpatterns = [
     path('', homeView, name = "homePage"),
     path('table/', tableView, name = "tablePage"),

]