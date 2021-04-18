from rest_framework import serializers
from .models import Tenent
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.views import Token
from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth.models import User
from django.conf import settings


class TenentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Tenent.objects.all())]
            )
    
    # hidden = serializers.BooleanField(default=False)
    # password=User.objects.make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889@#$%*")
    is_active =serializers.BooleanField(default=False)
    class Meta:
        model = Tenent
        fields =['id','shop_name','username', 'password','email','date_joined','phone_number','category','last_login','is_active']
        extra_kwargs ={'password':{
            'write_only':True,
           
        }}
    # def create(self, validated_data):
    #     tenent= Tenent.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         date_joined=validated_data['date_joined']
    #         # hidden =validated_data['hidden ']
    #         # hidden_by=validated_data['hidden_by']
    #     )
    #     password = User.objects.make_random_password( )
    #     tenent.set_password(password)
    #     tenent.save()

    def create(self,validated_data):
        tenent=Tenent.objects.create_user(**validated_data)
        print(tenent)
        # user=Tenent.objects.get(username=tenent)
        # Token.objects.create(user=tenent)
        return tenent
