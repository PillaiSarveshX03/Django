from . import views
from django.urls import path

urlpatterns = [

    path('Transaction',views.TransactionLC.as_view(),name='transaction'),
    path('Transaction/<int:pk>',views.TransactionRUD.as_view(),name='transaction'),

    
]


