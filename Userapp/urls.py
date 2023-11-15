from django.urls import path
from .views import UserRegisterView,AddMoneyView,FilterMoney
urlpatterns = [
    path("register/", UserRegisterView.as_view()),
    path("money/",AddMoneyView.as_view()),
    path("chiqim/",FilterMoney.as_view())
]
