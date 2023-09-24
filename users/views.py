from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from .forms import UserCommonFields, UserPicFields, UserSpecialFields, UserPasswordFields


# Create your views here.

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect(request.GET['next'] if 'next' in request.GET else 'home')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(email=username)
        except:
            messages.error(request, 'Username OR password is incorrect')
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        else:
            messages.error(request, 'Username OR password is incorrect')
    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


class AccountProfile(TemplateView):
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        current_user = request.user
        user_common_form = UserCommonFields(instance=current_user)
        user_pic_form = UserPicFields(instance=current_user)
        user_special_form = UserSpecialFields(instance=current_user)
        user_password_form = UserPasswordFields(user=current_user)
        context = {
            'user_common_form': user_common_form,
            'user_pic_form': user_pic_form,
            'user_special_form': user_special_form,
            'user_password_form': user_password_form,
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        current_user = request.user
        form_info = request.POST
        if form_info.get('form_type') == 'commonsbmt':
            user_common_form = UserCommonFields(form_info, instance=current_user)
            if user_common_form.is_valid():
                user_common_form.save()
        elif form_info.get('form_type') == 'picturesbmt':
            user_pic_form = UserPicFields(form_info, request.FILES, instance=current_user)
            if form_info.get('Delete') == 'delete':
                current_user.profile_image.delete(save=True)
            if user_pic_form.is_valid():
                user_pic_form.save()
        elif form_info.get('form_type') == 'specialsbmt':
            user_special_form = UserSpecialFields(form_info, instance=current_user)
            if user_special_form.is_valid():
                user_special_form.save()
        elif form_info.get('form_type') == 'passwordsbmt':
            user_password_form = UserPasswordFields(form_info, user=current_user)
            if user_password_form.is_valid():
                user_password_form.save()
        return redirect("/users/profile/")
