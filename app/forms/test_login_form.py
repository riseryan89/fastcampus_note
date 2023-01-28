from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'invalid': '잘못된 이메일 이잖아~~',
        })
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')

    def clean(self):
        email = self.cleaned_data.get("email")

        if email.split("@")[1] == "gmail.com":
            self.add_error('email', "Gmail은 이용할 수 없습니다.")
