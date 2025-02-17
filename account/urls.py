from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('edit', views.edit_user, name='edit'),
    path('reg', views.register_user, name='signup')

]
