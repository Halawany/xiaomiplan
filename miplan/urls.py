from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from .views import plan_home_view, insert_plan_view, update_plan_view

urlpatterns = [
    path('', plan_home_view, name='home'),
    path('insert', insert_plan_view, name="insert"),
    path('update', update_plan_view, name="update"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
