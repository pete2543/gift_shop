from django.contrib.auth.forms import UserCreationForm

class RegisterFrom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields