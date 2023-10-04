from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email','password')
        extra_kwargs={'password':{'write_only':False}}
    
    def create(self, valid_data):
        user=User.objects.create_user(valid_data['username'],valid_data['email'],valid_data['password'])
        return user
