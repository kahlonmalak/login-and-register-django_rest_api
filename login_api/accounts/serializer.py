from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password

# from django.contrib.auth.models import User

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import update_last_login
from rest_framework import serializers

# from rest_auth.serializers import PasswordResetSerializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user
    
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
               
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
        
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            
        ) 
        
        
#    ...reset password ...
   
  

# class CustomPasswordResetSerializer(PasswordResetSerializer):
#     email = serializers.EmailField()
#     password_reset_form_class = ResetPasswordForm

#     def validate_email(self, value):
#         # Create PasswordResetForm with the serializer
#         self.reset_form = self.password_reset_form_class(data=self.initial_data)
#         if not self.reset_form.is_valid():
#             raise serializers.ValidationError(self.reset_form.errors)

#         ###### FILTER YOUR USER MODEL ######
#         if not get_user_model().objects.filter(email=value).exists():
#             raise serializers.ValidationError(_('Invalid e-mail address'))

#         return value

#     def save(self):
#         request = self.context.get('request')
#         # Set some values to trigger the send_email method.
#         opts = {
#             'use_https': request.is_secure(),
#             'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
#             'request': request,
#         }
#         opts.update(self.get_email_options())
#         self.reset_form.save(**opts)     
        
        
# class ChangePasswordSerializer(serializers.Serializer):
#     model = User

#     """
#     Serializer for password change endpoint.
#     """
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)                   


class ChangePasswordSerializer(serializers.Serializer):


    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = (
            'old_password','new_password'
            
        ) 