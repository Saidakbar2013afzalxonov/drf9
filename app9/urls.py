# from django.urls import path
# from . import views

# urlpatterns = [
#     path("phones/", views.PhonesListAPIView.as_view(), name="phones-list"),
#     path("phones/create/", views.PhonesCreateAPIView.as_view(), name="phones-create"),
#     path("phones/<int:pk>/", views.PhonesRetrieveAPIView.as_view(), name="phones-detail"),
#     path("phones/<int:pk>/update/", views.PhonesUpdateAPIView.as_view(), name="phones-update"),
#     path("phones/<int:pk>/delete/", views.PhonesDestroyAPIView.as_view(), name="phones-delete"),
#     path("phones/list-create/", views.PhonesListCreateAPIView.as_view(), name="phones-list-create"),
#     path("phones/<int:pk>/retrieve-update/", views.PhonesRetrieveUpdateAPIView.as_view(), name="phones-retrieve-update"),
#     path("phones/<int:pk>/retrieve-destroy/", views.PhonesRetrieveDestroyAPIView.as_view(), name="phones-retrieve-destroy"),
#     path("phones/<int:pk>/retrieve-update-destroy/", views.PhonesRetrieveUpdateDestroyAPIView.as_view(), name="phones-retrieve-update-destroy"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('phones/', views.PhoneList, name='phone-list'),
    path('phone/<int:pk>/', views.PhoneView, name='phone-view'),
    path('phone/create/', views.PhoneCreate, name='phone-create'),
    path('phone/update/<int:pk>/', views.PhoneUpdate, name='phone-update'),
    path('phone/delete/<int:pk>/', views.PhoneDelete, name='phone-delete'),

    path('phones-list-create/', views.PhoneListCreate, name='phone-list-create'),
    path('phone-detail/<int:pk>/', views.PhoneDetail, name='phone-detail'),
]