from django.urls import path
from django.conf.urls import include
from .views import home, contato, servicos

urlpatterns = [
    path('', home, name='website_home'),
    path('contato/', contato, name='website_contato'),
    path('servicos/', servicos, name='website_servicos'),
]
