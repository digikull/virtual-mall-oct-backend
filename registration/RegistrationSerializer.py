from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model() #For Custom User

#Creating RegistrationSerializer
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name','password', 'email']

        #Validating the email
        def validate(self, attrs):
            email = attrs.get('email', '')
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    {'email': 'email is Already used'}
                )
            return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data) 