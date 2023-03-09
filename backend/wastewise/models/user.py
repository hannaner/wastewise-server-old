from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionMixin, BaseUserManager
from django.conf import settings
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    """Manager for user profiles"""
    
    ### Create new user profile
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Need to enter valud email address')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # hash password
        user.set_password(password)
        user.save()
        return user
    
    ### Create superuser (admin)
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionMixin):
    """Database model for users"""
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    # set auth token
    def get_auth_token(self):
        Token.objects.filter(user=self).delete()
        token = Token.objects.create(user=self)
        self.token = token.key
        self.save()
        return token.key
    
    # remove auth token
    def delete_token(self):
        Token.objects.filter(user=self).delete()
        self.token = None
        self.save()
        return self