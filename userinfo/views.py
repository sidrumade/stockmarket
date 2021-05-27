from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UserProfileInfoForm, UserProfileLoginForm
from django.shortcuts import reverse, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.views.decorators.cache import cache_control


# Create your views here.

class UserInfoFormView(FormView):
    form_class = UserProfileInfoForm
    template_name = 'userinfo/registration.html'

    def get_success_url(self):
        return reverse('userinfo:registration')

    def form_valid(self, form):
        '''this method is called when form has been posted'''
        form.save_user(form)

        return super().form_valid(form)


class UserProfileLoginFormView(FormView):
    form_class = UserProfileLoginForm
    template_name = 'userinfo/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: #user shold not access login page again if he already authenticated
            return redirect('index')
        return render(request,self.template_name,context={'form':self.get_form()})

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            print('you are authenticated')
        else:
            print('not authenticated')
        '''this method is called when form has been posted'''

        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if not user:
            messages.error(self.request, 'username or password not correct')
            return redirect('userinfo:login')
        elif not user.is_active:
            messages.error(self.request, 'username is not active')
            return redirect('userinfo:login')
        else:
            login(self.request, user)
            return redirect('index')

        return super().form_valid(form)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)  # this clear cache after logout
def logout_user(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        logout(request)  # logout authenticated user
        return redirect('index')  # go to index page after logout
