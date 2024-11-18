
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.db.utils import IntegrityError
from .services import crear_usuario

# Create your views here.
def index(request):
    return render(request, 'index.html')


class RegisterUser(View):
    def dipatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        username = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        if password != password_repeat:
            messages.error(request, 'Password does not match')
            return(render, 'registration/register.html')
        try:
            crear_usuario(username, first_name, last_name, email, password)
        except IntegrityError:
            messages.error(request, 'The email already exist')
            return(render, 'registration/register.html')

        messages.success(request, 'Congrats! your user was created succesfully. Please Log in')
        return redirect('login')
    def get(self, request):
        return render(request, 'registration/register.html')