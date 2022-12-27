from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='homepage' ),
    path('add/', views.addemployee, name='add'),
    path('edit/',views.editEmployee, name='edit'),
    path('update/<str:id>', views.updateEmployee, name='update'),#<str or int:id> both working
    path('delete/<int:id>', views.deleteEmployee, name='delete')
]