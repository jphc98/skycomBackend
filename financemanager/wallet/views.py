from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from wallet import models, serializers
from rest_framework import viewsets


class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializers
    queryset = models.User.objects.all()

class TypeBillView(viewsets.ModelViewSet):
    serializer_class = serializers.TypeBillSerializers
    queryset = models.TypeBill.objects.all()

class BillView(viewsets.ModelViewSet):
    serializer_class = serializers.BillSerializers
    queryset = models.Bill.objects.all()

class TypeIncomeView(viewsets.ModelViewSet):
    serializer_class = serializers.TypeIncomeSerializers
    queryset = models.TypeIncome.objects.all()

class IncomeView(viewsets.ModelViewSet):
    serializer_class = serializers.IncomeSerializers
    queryset = models.Income.objects.all()

class TypeSavingTargetView(viewsets.ModelViewSet):
    serializer_class = serializers.TypeSavingTargetSerializers
    queryset = models.TypeSavingTarget.objects.all()

class SavingTarget(viewsets.ModelViewSet):
    serializer_class = serializers.SavingTargetSerializers
    queryset = models.SavingTarget.objects.all()



