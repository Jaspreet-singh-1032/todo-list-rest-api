# rest framework imprts
from rest_framework import serializers

# model imports
from app.models import (
    User ,
    TodoList
)

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' , 'username' , 'password')
        extra_kwargs = {
            'password':{'write_only':True}
        }

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username' , 'email')
        extra_kwargs = {
            'username':{'required':False}
        }

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id' , 'task' , 'description' , 'datetime' , 'is_completed')