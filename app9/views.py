from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import Phones
from .serializers import PhonesSerializer


class PhonesListAPIView(ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer


class PhonesRetrieveAPIView(RetrieveAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer


class PhonesCreateAPIView(CreateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer


class PhonesUpdateAPIView(UpdateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer


class PhonesDestroyAPIView(DestroyAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer


class PhonesListCreateAPIView(ListCreateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer


class PhonesRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer


class PhonesRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer


class PhonesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
