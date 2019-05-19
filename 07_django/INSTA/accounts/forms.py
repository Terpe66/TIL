from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
# UserCreationForm: 가입, UserChangeForm: 정보 수정, AuthenticationForm: 로그인
from .models import User


class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User


class CustomUserChaneForm(UserChangeForm):
    pass
