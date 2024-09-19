from rest_framework import serializers
from wallet import models

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class BillSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Bill
        fields = '__all__'

class IncomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Income
        fields = '__all__'

class SavingTargetSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SavingTarget
        fields = '__all__'

class TypeBillSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.TypeBill
        fields = '__all__'

class TypeIncomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.TypeIncome
        fields = '__all__'

class TypeSavingTargetSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.TypeSavingTarget
        fields = '__all__'