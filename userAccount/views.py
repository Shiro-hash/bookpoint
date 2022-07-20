from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import AccountAuthenticationForm, UserRegistrationForm


class SignUpView(CreateView):
    form_class = UserRegistrationForm
    get_success_url = ''
    template_name = 'userAccount/registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.AllowAllUsersModelBackend')
        return HttpResponseRedirect(self.get_success_url)


def login_view(request, *args, **kwargs):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home') #Will change

    if request.POST:
        form = AccountAuthenticationForm
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('home')
            else:
                context['login_form'] = form

    return render(request, 'userAccount/login.html', context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get(next))
    return redirect

def logout_view(request):
    logout(request)
    return redirect('home')
