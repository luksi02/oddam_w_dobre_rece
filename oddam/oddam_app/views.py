from django.http import request
from django.shortcuts import render
from django.views import View

from oddam_app.models import Donation, Institution, Category




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

        print(Institution.objects.get(id=1).categories)

        return render(request, 'index.html', {'liczba_wspartych_organizacji':liczba_wspartych_organizacji,
                                              'liczba_oddanych_workow':liczba_oddanych_workow,
                                              'institutions_foundations':institutions_foundations,
                                              'institutions_organisations':institutions_organisations,
                                              'institutions_local':institutions_local})

class LoginView(View):

    def get(self, request):

        return render(request, 'login.html')
    

class AddDonationView(View):

    def get(self, request):

        return render(request, 'form.html')
    
    
class RegisterView(View):

    def get(self, request):

        return render(request, 'register.html')
