from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User

from oddam_app.models import Donation, Institution, Category, CategoryInstitution

from oddam_app.forms import RegisterForm


# Create your views here.
class IndexView(View):

    def get(self, request):

        donations_list = Donation.objects.all()
        liczba_oddanych_workow = 0
        liczba_wspartych_organizacji = 0
        for donation in donations_list:
            liczba_oddanych_workow = liczba_oddanych_workow + donation.quantity
            liczba_wspartych_organizacji = liczba_wspartych_organizacji + 1

        institutions_foundations = Institution.objects.filter(type=0)
        institutions_organisations = Institution.objects.filter(type=1)
        institutions_local = Institution.objects.filter(type=2)

        return render(request, 'index.html', {'liczba_wspartych_organizacji':liczba_wspartych_organizacji,
                                              'liczba_oddanych_workow':liczba_oddanych_workow,
                                              'institutions_foundations':institutions_foundations,
                                              'institutions_organisations':institutions_organisations,
                                              'institutions_local':institutions_local})

class LoginView(View):

    def get(self, request):
     return render(request, 'login.html')

    def post(self, request):
        login_username = request.POST.get("email")
        login_password = request.POST.get("password")
        user = authenticate(request, username=login_username, password=login_password)
        if user is not None:
            login(request, user)
            url = request.GET.get('next', 'index')#work work work
            return redirect(url)
        elif not User.objects.filter(username=login_username):
            return redirect(reverse('register'))
        else:
            return render(request, 'login.html', {'message': "Niepoprawne dane!"})


class AddDonationView(LoginRequiredMixin, View):

    def get(self, request):

        categories = Category.objects.all()
        categories_institutions = CategoryInstitution.objects.all()
        institutions = Institution.objects.all()

        return render(request, 'form.html', {'categories': categories,
                                             'institutions': institutions,
                                             'categories_institutions': categories_institutions})

    
class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("email")
        password1 = request.POST.get("password")
        password2 = request.POST.get("password2")
        #user = authenticate(request, username=username, password=password)
        if username and password1 == password2:
            password = password1
            user = User.objects.create(first_name=first_name, last_name=last_name, username=username)
            user.set_password(password)
            user.save()
            return redirect(reverse('login'))
        return render(request, 'register.html', {'message':"Niepoprawne dane!"})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('index'))


class UserDetailsView(LoginRequiredMixin, View):

    def get(self, request, id):

        user = get_object_or_404(User, id=id)
        return render(request, 'user_details.html', {'user':user})

class PasswordBeforeSettings(View):

    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        return render(request, 'password_check.html', {'user':user})

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        password_checked = request.POST.get("password")
        #try with authenticate(user=user, password=password_input"
        print(user.password)
        user = authenticate(request, username=user.username, password=password_checked)
        if user is not None:
            print('hello_word')
            url = reverse('change_user_settings', args=(id,))
            return redirect(url)
        return render(request, 'password_check.html', {'message':"Niepoprawne dane!"})


class ChangeUserSettingsView(View):

    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        return render(request, 'change_user_settings.html')

    """def post(self, request, id):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("email")
        password1 = request.POST.get("password")
        password2 = request.POST.get("password2")
        #user = authenticate(request, username=username, password=password)
        if username and password1 == password2:
            password = password1
            user = User.objects.create(first_name=first_name, last_name=last_name, username=username)
            user.set_password(password)
            user.save()
            return redirect(reverse('login'))
        return render(request, 'register.html', {'message':"Niepoprawne dane!"})"""