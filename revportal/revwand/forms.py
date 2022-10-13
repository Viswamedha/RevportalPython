# Imports
from django.forms import Form, ModelForm, TextInput, DateInput, EmailInput, CharField, PasswordInput, SelectDateWidget, EmailField
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.hashers import check_password
from datetime import datetime, timedelta
from .models import RevportalUser
from django import forms 


class CreateRevportalUserForm(ModelForm):

    password = CharField(
        widget = PasswordInput(
            attrs = {
            'class': 'form-control inputarea password',
            'placeholder': "Enter Password Here",
            'id': 'password',
            'name': 'new-password'
            }
        )
    )
    confirm_password = CharField(
        widget = PasswordInput(
            attrs = {
                'class': 'form-control inputarea password',
                'placeholder': "Confirm Password Here",
                'name': 'new-password',
                'id': 'confirm'
            }
        )
    )


    class Meta:
        model = RevportalUser
        fields = ('email_address', 'username', 'date_of_birth', 'first_name', 'last_name', 'middle_name', 'phone_number')
        widgets = {
            'email_address': EmailInput(
                attrs = {
                    'class': 'form-control inputarea email',
                    'placeholder': "Enter Email Address",
                    'id': 'email',
                    'name': 'email',
                }
            ),
            'username': TextInput(
                attrs = {
                    'class': 'form-control inputarea',
                    'placeholder': "Username",
                    'id': 'username',
                    'name': 'username'
                }
            ),
            'date_of_birth': DateInput(
                attrs = {
                    'class': 'form-control',
                    'style': 'color: rgb(110, 110, 110);',
                    'max': (datetime.now()-timedelta(days=10*365)).strftime("%d/%m/%Y"),
                    'min': (datetime.now()-timedelta(days=70*365)).strftime("%d/%m/%Y")
                }
            ),
            'first_name': TextInput(
                attrs = {
                    'class': 'form-control inputarea',
                    'placeholder': "Username",
                    'id': 'username',
                    'name': 'username'
                }
            ),
            'last_name': TextInput(
                attrs = {
                    'class': 'form-control inputarea',
                    'placeholder': "Username",
                    'id': 'username',
                    'name': 'username'
                }
            ),
            'middle_name': TextInput(
                attrs = {
                    'class': 'form-control inputarea',
                    'placeholder': "Username",
                    'id': 'username',
                    'name': 'username'
                }
            ),
            'phone_number': TextInput(
                attrs = {
                    'class': 'form-control inputarea',
                    'placeholder': "Username",
                    'id': 'username',
                    'name': 'username'
                }
            ),
        }


    def save(self, commit=True):
        if self.cleaned_data["password"] and self.cleaned_data["confirm_password"] and self.cleaned_data["password"] == self.cleaned_data["confirm_password"]: 
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["confirm_password"])
            if commit: user.save()
            return user
        return None

class EditRevportalUserForm(ModelForm):
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = RevportalUser
        fields = ('email_address', 'date_of_birth', 'first_name', 'last_name', 'phone_number')
        widgets = {
            'date_of_birth': SelectDateWidget(years=[str(i) for i in range(int(datetime.now().year)-70, int(datetime.now().year)-10)][::-1])  
        }

    def clean_password(self): 
        return self.initial["password"]


class LoginRevportalUserForm(Form):
    email = EmailField(
        widget = EmailInput(
            attrs = {
                'class': 'form-control inputarea email',    
                'placeholder': "Enter Email Address",
            }
        )
    )
    password = CharField(
        widget = PasswordInput(
            attrs = {
                'class': 'form-control inputarea password',
                'placeholder': "Enter Password Here",
                'id': 'password'
            }
        )
    )
    
    def is_valid_user(self):
        try: 
            user = RevportalUser.objects.get(email=self.cleaned_data.get('email'))
        except: 
            user = None
        if user and check_password(self.cleaned_data.get('password'), user.password): 
            return user
        else: 
            return None


class ResetRequestForm(Form):
    email = EmailField(widget=TextInput(attrs = {
        'placeholder': 'Enter Email Address Here'
    }))
    
    def validate(self):
        try:
            user = RevportalUser.objects.get(email=self.cleaned_data["email"])
            if user: 
                if user.is_verified:
                    return user
            return False
        except Exception as e: 
            print(e)
            return False


class ResetPasswordForm(ModelForm):
    password_1 = CharField(label='Password', widget=PasswordInput(
        attrs = {
            'placeholder': 'Enter New Password Here',
            'style': 'color: white;'
        }
    ))
    password_2 = CharField(label='Confirm Password', widget=PasswordInput(
        attrs = {
            'placeholder': 'Confirm New Password Here',
            'style': 'margin-bottom: 4rem; color: white;'
        }
    ))

    class Meta:
        model = RevportalUser
        fields = ()
    
    def validate(self):
        if self.cleaned_data['password_1'] == self.cleaned_data['password_2']:
            self.instance.set_password(self.cleaned_data['password_1'])
            self.instance.save()
            return True
        return False



