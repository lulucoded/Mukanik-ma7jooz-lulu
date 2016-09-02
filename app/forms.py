from django import forms
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse


#crispy imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Div, Field
from crispy_forms.bootstrap import FormActions

#user login 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm  
from app.models import CustomUser



class CustomUserCreationForm(UserCreationForm):  
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # del self.fields['email']

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):  
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = '__all__'



class CustomUserLoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = '/login'
        self.helper.layout = Layout(
                    Div('email'),
                    Div('password'),
                    Div(
                        FormActions(
                            Submit('submit', 'Sign Up'),
                            ),
                        )
                    )