from django.urls import path

from .views import ComplexAPIView

app_name = 'build'

urlpatterns = [
    path('', ComplexAPIView.as_view(), name='create_residential_complex'),

]
