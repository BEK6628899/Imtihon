from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


class SuvViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]




class MijozViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        queryset =Mijoz.objects.filter(user=self.request.user)
        return queryset
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(serializer.data)



class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        queryset =Admin.objects.filter(user=self.request.user)
        return queryset
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(serializer.data)



class HaydovchiViewSet(ModelViewSet):
    queryset = Haydovchi.objects.all()
    serializer_class = HaydovchiSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]




class BuyurtmaViewSet(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        queryset = [Buyurtma.objects.filter(mijoz__user=self.request.user),
                    Buyurtma.objects.filter(admin__user=self.request.user)]
        return queryset
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(serializer.data)




