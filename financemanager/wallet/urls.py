from django.urls import path, include
from rest_framework import routers
from wallet import views

router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'users')
router.register(r'type/bills', views.TypeBillView, 'type_bills')
router.register(r'bills', views.BillView, 'bills')
router.register(r'type/incomes', views.TypeIncomeView, 'type_incomes')
router.register(r'incomes', views.IncomeView, 'incomes')
router.register(r'type/saving/targets', views.TypeSavingTargetView, 'type_saving_targets')
router.register(r'saving/targets', views.SavingTarget, 'saving_targets')
##

urlpatterns = [
    path('api/', include(router.urls)),    
]