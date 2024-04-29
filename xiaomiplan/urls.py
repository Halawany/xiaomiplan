from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miplan.urls')),
    path('accounts/', include('allauth.urls')),
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name='account_login'),
    # path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='account_logout'),
]
