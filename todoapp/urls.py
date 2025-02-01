from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup, name="signup"),
    path('login/',views.user_login, name='login'),
    path('todo/',views.todo, name='todo'),
    path('delete/<int:srno>', views.delete_todo),
    path('edit/<int:srno>', views.edit_todo, name='edit'),
    path('signout/', views.signout, name='signout')
]
