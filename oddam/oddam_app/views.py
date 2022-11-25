from django.http import request
from django.shortcuts import render
from django.views import View

from oddam_app.models import Donation


# Create your views here.
class IndexView(View):

    def get(self, request):

        donations_list = Donation.objects.all()
        liczba_oddanych_workow = 0
        liczba_wspartych_organizacji = 0
        for donation in donations_list:
            liczba_oddanych_workow = liczba_oddanych_workow + donation.quantity
            liczba_wspartych_organizacji = liczba_wspartych_organizacji + 1

        return render(request, 'index.html', {'liczba_wspartych_organizacji':liczba_wspartych_organizacji, 'liczba_oddanych_workow':liczba_oddanych_workow})

class LoginView(View):

    def get(self, request):

        return render(request, 'login.html')
    

class AddDonationView(View):

    def get(self, request):

        return render(request, 'form.html')
    
    
class RegisterView(View):

    def get(self, request):

        return render(request, 'register.html')
