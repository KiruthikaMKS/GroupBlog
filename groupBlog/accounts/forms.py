from django.contrib.auth.forms import UserCreationForm
from accounts.models import myUser

class NewUserForm(UserCreationForm):
    class Meta:
        model = myUser
        fields = ('username','email','password1','password2')

        def __init__(self,*args,**kwargs):
            context = super().__init__(*args,**kwargs)
            context['username'] = 'DisplayName'
            context['email'] = 'Email Address'
