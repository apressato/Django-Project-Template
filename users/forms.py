from django.forms import ModelForm, PasswordInput
from django import forms
from django.forms import Widget
from django.forms.widgets import Input
from django.utils.safestring import mark_safe
from .models import ExtendedUser
from django.contrib.auth.forms import PasswordChangeForm
class UserCommonFields(ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ['first_name', 'last_name',  'Short_Intro', 'Social_LinkedIn', 'Social_Instagram', 'Social_facebook',
                  'CultureId', 'Screen_scale']
        labels = {'first_name': '',
                  'last_name': '',
                  'Short_Intro': 'Short Intro',
                  'Social_LinkedIn': '',
                  'Social_Instagram': '',
                  'Social_facebook': '',
                  'CultureId': '',
                  'Screen_scale': '',
                  }
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
                   'Short_Intro': forms.Textarea(attrs={'class':'form-control django-ckeditor-widget ckeditor',
                                                        'placeholder': 'Short Intro'}),
                   'Social_LinkedIn': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Linkedin'}),
                   'Social_Instagram': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Instagram'}),
                   'Social_facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Facebook'}),
                   'CultureId': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Your Language'}),
                   'Screen_scale': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Screen Scale'})}
    def __init__(self, *args, **kwargs):
        super(UserCommonFields, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
class UserPicFields(ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ['profile_image', 'UseGravatar']
    def __init__(self, *args, **kwargs):
        super(UserPicFields, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
class UserSpecialFields(ModelForm):
    class Meta:
        model = ExtendedUser
        fields =['username', 'email']
    def __init__(self, *args, **kwargs):
        super(UserSpecialFields, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        labels = {'username': '',
                  'email': ''}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'})}
class PasswordInputWithButtons(Input):
    input_type = "password"
    template_name = "users/_macros/_PasswordInputWithButtons.html"
    def __init__(self, attrs=None, render_value=False):
        super().__init__(attrs)
        self.render_value = render_value
    def get_context(self, name, value, attrs):
        if not self.render_value:
            value = None
        return super().get_context(name, value, attrs)
class UserPasswordFields(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
    # widget = {
    #     'old_password': PasswordInputWithButtons(),
    #     'new_password1': PasswordInputWithButtons(),
    #     'new_password2': PasswordInputWithButtons(),
    # }
