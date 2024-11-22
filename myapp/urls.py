from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('loginn/', views.loginn, name='login'),
    path('todopage/', views.todo, name='todopage'),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>', views.delete_todo, name='delete_todo'),
    path('signout/',views.signout, name = 'signout')
]

