from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Account Created Successfully!")
            return redirect('user_login')
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'form': register_form})


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Account Updated Successfully!")
            return redirect('edit_profile')
        else:
            messages.error(request, "Invalid Data!")
    else:
        profile_form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': profile_form})


class UserLogin(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "Logged In Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid Data!")
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
    # next_page = reverse_lazy('user_login')
    def get_success_url(self):
        messages.success(self.request, "Logged Out Successfully!")
        return reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class UserPasswordChange(PasswordChangeView):
    template_name = 'change_password.html'

    def get_success_url(self):
        return reverse_lazy('change_password')

    def form_valid(self, form):
        messages.success(self.request, "Password Updated Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid Data!")
        return super().form_invalid(form)

@method_decorator(login_required, name='dispatch')
class UserPasswordReset(PasswordResetView):
    template_name = 'reset_password.html'

    def get_success_url(self):
        return reverse_lazy('reset_password')

    def form_valid(self, form):
        messages.success(self.request, "Password Reset Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid Data!")
        return super().form_invalid(form)
    
@login_required
def change_password_without_old(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('change_password_without_old')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'change_password_without_old.html', {'form': form})