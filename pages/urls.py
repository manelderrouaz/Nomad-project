from django.urls import path
from . import views

urlpatterns = [
    path('', views.destiantion, name='main_part'),
    path('Destination', views.destiantion, name='destination'),
    path('Search', views.search_dest, name='search-dest'),
    path('guide',views.guide, name='guide'),
    path('DevenirGuide',views.DevenirGuide, name='DevenirGuide'),
    path('formcovoiturage',views.formcovoiturage, name='formcovoiturage'),
    path('MyAccount', views.accept, name='MyAccount'),
    path('Mesdemandes',views.Mesdemandes, name='Mesdemandes'),
    path('carsettings', views.carset, name='carsettings'),
    path('carinfo', views.carinfo, name='carinfo'),
    path('covoiturage',views.covoiturage, name='covoiturage'),

]
