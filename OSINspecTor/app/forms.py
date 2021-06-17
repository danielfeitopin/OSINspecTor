from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class SignupFrom(forms.Form,UserCreationForm):
   def __init__(self, *args, **kwargs):
       super(SignupFrom,self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id_registerForm'
       self.helper.form_class = 'form-group'
       self.helper.form_method = 'post'
       self.helper.form_action = 'signup_view'
       self.helper.add_input(Submit('registrar', 'Registrar'))

class RegisterForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )       

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
        ButtonHolder(
            Submit('login', 'Login', css_class ='btn-primary')
        )
    )