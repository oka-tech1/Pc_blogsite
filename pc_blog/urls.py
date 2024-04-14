from django.urls import path
from .views import mypc
from . import views



urlpatterns = [
    path('pc_blog/', mypc.as_view(), name='pc'),
    path('pc_blog/details/<int:id>', views.details, name='details'),
    path('', views.home, name='home'),

]
