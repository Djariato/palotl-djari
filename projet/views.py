from django.shortcuts import render

# Create your views here.
from django.views import View


class Exer(View):
    def get(self, request):
        cont = {

        }
        return render(request, 'dja.html', context=cont)