from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret_page'),
    path('password/change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password/change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password/reset/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password/reset/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/', include('django.contrib.auth.urls')),

]
