from . import views
from django.urls import path

urlpatterns = [

    path('Turf',views.TransactionLC.as_view(),name='Turf'),
    path('Turf/<int:pk>',views.TransactionRUD.as_view(),name='Turf'),

    
]


