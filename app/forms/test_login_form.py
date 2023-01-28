import re

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from app.models import UserDetail


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "invalid": "잘못된 이메일 이잖아~~",
        },
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Password")

    def clean(self):
        email = self.cleaned_data.get("email")

        if email.split("@")[1] == "gmail.com":
            self.add_error("email", "Gmail은 이용할 수 없습니다.")


class SignupForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "유저명"}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "이메일 주소"}),
        error_messages={
            "invalid": "잘못된 이메일 이잖아~~",
        },
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "비밀번호"}), label="Password1"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "비밀번호 확인"}),
        label="Password2",
        error_messages={
            "password_mismatch": "비밀번호가 일치하지 않습니다.",
        },
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def clean(self):
        username = self.cleaned_data.get("username")

        if not re.match("^[a-z0-9_]*$", username):
            self.add_error("username", "소문자와, 숫자, 언더스코어(_) 만 사용가능!")

        if self.cleaned_data.get("password") is not None:
            try:
                validate_password(self.cleaned_data.get("password"))
            except ValidationError as e:
                self.add_error("password1", "사용할 수 없는 패스워드")
        email = self.cleaned_data.get("email")
        user = get_user_model()
        if email is not None:
            dupe_date = user.objects.filter(email=email).exists()
            if dupe_date:
                self.add_error("email", "이미 존재하는 이메일 입니다.")

        dupe_date = user.objects.filter(username=username).exists()
        if dupe_date:
            self.add_error("username", "이미 존재하는 유저명 입니다.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data.get("password1"))
        if commit:
            user.save()
            UserDetail.objects.create(user=user, note_count=0)

        return user
