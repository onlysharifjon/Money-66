from django.urls import path
from .views import UserRegisterView,AddMoneyView
urlpatterns = [
    path("register/", UserRegisterView.as_view()),
    path("money/",AddMoneyView.as_view())
]
