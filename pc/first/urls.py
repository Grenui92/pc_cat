from django.urls import path
from .views import create_cats, all_cats, create_tovar, show_tovar
app_name = 'first'

urlpatterns = [
    path('create/', create_cats), 
    path('create_tovar/', create_tovar),
    path('all/', all_cats),
    path('show_tovar/', show_tovar)
]
