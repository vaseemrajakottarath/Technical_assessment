from django.contrib.auth.backends import BaseBackend
from .models import User
from django.contrib.auth.hashers import check_password


class CustomAuthenticationBackend(BaseBackend):

    def authenticate(*email_phone):
        try:
            try:
                user = User.objects.get(email=email_phone[0])
            except:
                user = User.objects.get(phone_number=email_phone[0])
        except:
            return None
        password_valid = check_password(email_phone[1],user.password)
        if user and password_valid:
            return user
        return None 
