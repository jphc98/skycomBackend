from django.contrib import admin
from .models import User, TypeBill, Bill, TypeIncome, Income, TypeSavingTarget, SavingTarget

admin.site.register(User)
admin.site.register(TypeBill)
admin.site.register(Bill)
admin.site.register(TypeIncome)
admin.site.register(Income)
admin.site.register(TypeSavingTarget)
admin.site.register(SavingTarget)

# Register your models here.
