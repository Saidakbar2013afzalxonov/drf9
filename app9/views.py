# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
# from .models import Phones
# from .serializers import PhonesSerializer


# class PhonesListAPIView(ListAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhonesSerializer


# class PhonesRetrieveAPIView(RetrieveAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhonesSerializer


# class PhonesCreateAPIView(CreateAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhonesSerializer


# class PhonesUpdateAPIView(UpdateAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhonesSerializer


# class PhonesDestroyAPIView(DestroyAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhonesSerializer


# class PhonesListCreateAPIView(ListCreateAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhonesSerializer


# class PhonesRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhonesSerializer


# class PhonesRetrieveDestroyAPIView(RetrieveDestroyAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhonesSerializer


# class PhonesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhonesSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Phones
from .serializers import PhonesSerializer


@api_view(['GET'])
def PhoneList(request):
    phones = Phones.objects.all()
    serializer = PhonesSerializer(phones, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def PhoneView(request, pk):
    phone = Phones.objects.get(pk=pk)
    serializer = PhonesSerializer(phone)
    return Response(serializer.data)


@api_view(['POST'])
def PhoneCreate(request):
    serializer = PhonesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(
        {"message": "Ma'lumotlar noto'g'ri kiritildi!"},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['PUT', 'PATCH'])
def PhoneUpdate(request, pk):
    phone = Phones.objects.get(pk=pk)

    serializer = PhonesSerializer(phone, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(
        {"message": "Telefonni yangilashda xatolik yuz berdi!"},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['DELETE'])
def PhoneDelete(request, pk):
    phone = Phones.objects.get(pk=pk)
    phone.delete()

    return Response(
        {"message": "Telefon o'chirildi!"},
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'POST'])
def PhoneListCreate(request):
    if request.method == 'GET':
        phones = Phones.objects.all()
        serializer = PhonesSerializer(phones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PhonesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            {"message": "Ma'lumotlar noto'g'ri kiritildi!"},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def PhoneDetail(request, pk):
    phone = Phones.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = PhonesSerializer(phone)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PhonesSerializer(phone, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            {"message": "Telefonni to'liq yangilashda xatolik yuz berdi!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'PATCH':
        serializer = PhonesSerializer(phone, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            {"message": "Telefonni qisman yangilashda xatolik yuz berdi!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        phone.delete()
        return Response(
            {"message": "Telefon muvaffaqiyatli o'chirildi!"},
            status=status.HTTP_204_NO_CONTENT
        )
