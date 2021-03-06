from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Obrigatório. Informe um endereço de email válido. Apenas emails da UnB são aceitos', validators=[RegexValidator(regex=r'^[\w\d\.]*@(?:aluno\.)?unb\.br$', message='Só são permitidos emails da UnB.', code='invalid_email'),])
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')