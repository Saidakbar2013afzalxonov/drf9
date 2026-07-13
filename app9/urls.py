from django.urls import path
from .views import PhonesViewSet

urlpatterns = [
    path('', PhonesViewSet.as_view({'post': 'create'})),
]