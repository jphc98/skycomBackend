from django.db import models
from django.contrib.postgres.fields import JSONField

#Usuarios
class User(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    surname = models.CharField('Apellido', max_length = 30)
    second_surname = models.CharField('Segundo apellido', max_length = 30)
    identification = models.SmallIntegerField(unique = True)
    birthdate = models.DateField('Fecha de nacimiento')
    email = models.EmailField('Correo electrónico', max_length = 60)

    def __str__(self):
        return self.name

#Tipos de gastos
class TypeBill(models.Model):
    name = models.CharField('Tipo de gasto', max_length = 70)
    description = models.TextField('Descripción')

    def __str__(self):
        return self.name

#Gastos
class Bill(models.Model):
    user = models.ForeignKey(User, verbose_name = 'Usuario', on_delete = models.CASCADE)
    amount = models.IntegerField('Monto')
    date = models.DateField('Fecha')
    category = models.ForeignKey(TypeBill, verbose_name = 'Tipo de gasto', on_delete = models.CASCADE)
    description = models.TextField('Descripción gasto')

    def __str__(self):
        return self.category

#Tipos de ingresos
class TypeIncome(models.Model):
    name = models.CharField('Tipo de ingreso', max_length = 70)
    description = models.TextField('Descripción')

    def __str__(self):
        return self.name

#Ingresos
class Income(models.Model):
    user = models.ForeignKey(User, verbose_name = 'Usuario', on_delete = models.CASCADE)
    amount = models.IntegerField('Monto')
    date = models.DateField('Fecha')
    category = models.ForeignKey(TypeIncome, verbose_name = 'Tipo de ingreso', on_delete = models.CASCADE)
    description = models.TextField('Descripción ingreso')

    def __str__(self):
        return self.category

#Tipos de ahorro
class TypeSavingTarget(models.Model):
    name = models.CharField('Tipo de ahorro', max_length = 70)
    description = models.TextField('Descripción')

    def __str__(self):
        return self.name

#Objetivos de ahorro
class SavingTarget(models.Model):
    user = models.ForeignKey(User, verbose_name = 'Usuario', on_delete = models.CASCADE)
    amount = models.IntegerField('Monto objetivo')
    start_date = models.DateField('Fecha de inicio')
    end_date = models.DateField('Fecha de finalización')
    category = models.ForeignKey(TypeSavingTarget, verbose_name = 'Tipo de ahorro', on_delete = models.CASCADE)
    description = models.TextField('Descripción ahorro')

    def __str__(self):
        return self.description






