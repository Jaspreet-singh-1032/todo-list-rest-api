# django imports
from django.contrib.auth import authenticate

# rest framework imports
from rest_framework import viewsets , mixins , generics
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response

# models imports
from app.models import (
    User , 
    TodoList
)
from rest_framework.authtoken.models import (
    Token
)

# serializer imports
from app.serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserSerializer,
    TodoListSerializer
)

# permissions imports
from rest_framework import permissions
from app.permissions import IsOwner

class UserRegisterViewSet( mixins.CreateModelMixin , viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self , request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response({"detail":"Registered successfully"} , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self , request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                token , created = Token.objects.get_or_create(user=user)
                return Response({"token":token.key} , status=status.HTTP_200_OK)
            else:
                return Response({"detail":"Wrong credentials"} , status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(mixins.ListModelMixin , 
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def list(self , request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data , status=status.HTTP_200_OK)

class TodoListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner]
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
    def perform_create(self , serializer):
        serializer.save(user = self.request.user)
    