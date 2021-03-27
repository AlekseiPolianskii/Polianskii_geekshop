from django.urls import path

from adminapp.views import index, admin_users, admin_users_create, admin_users_update, admin_users_delete,admin_users_rebuild

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('user-create/', admin_users_create, name='admin_users_create'),
    path('user-update/<int:user_id>/', admin_users_update, name='admin_users_update'),
    path('user-delete/<int:user_id>/', admin_users_delete, name='admin_users_delete'),
    path('user-rebuild/<int:user_id>/', admin_users_rebuild, name='admin_users_rebuild'),
]