from django.shortcuts import render
from .serializers import RegisterSerializer, AllMoneySerializer, User,AllMoney
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class UserRegisterView(APIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    def post(self, request):
        username=request.data.get('user_name')
        password=request.data.get('user_password')
        user = User.objects.create(user_name=username,user_password=password)
        user.save()
        return Response({"status":"User created"})

class AddMoneyView(APIView):
    serializer_class = AllMoneySerializer
    queryset = AllMoney.objects.all()
    def post(self,request):
        serializer = AllMoneySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"status 200 ok"})
        else:
            return Response(serializer.errors)

