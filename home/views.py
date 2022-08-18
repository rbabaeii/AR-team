from django.shortcuts import render
from django.views import View
from .models import Projects_model

# Create your views here.
class home_page(View):
    def get(self ,request):
        return render(request , "home/index.html")

class Anytwo(View):
    def get(self , request):
        return render(request , 'home/anytwo.html')
class Reza(View):
    def get(self , request):
        return render(request , 'home/reza.html')
class Amir(View):
    def get(self , request):
        return render(request , "home/amir.html")
class Madrak_R(View):
    def get(self , request):
        return render(request , 'home/madrak.html')
# class Project(View):
#     def get(self , request):
#         project = Projects_model.objects.all()
#         return render(request , 'home/project.html' , {'projects' : project})

class Madrak_A(View):
    def get(self , request):
        return render(request , "home/amirmadrak.html")