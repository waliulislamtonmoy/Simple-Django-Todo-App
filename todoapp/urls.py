

from django.urls import path
from .views import home,delete,update

urlpatterns = [
   path("",home),
   path("update/<int:id>/",update),
   path("delete/<int:id>/",delete)
]
