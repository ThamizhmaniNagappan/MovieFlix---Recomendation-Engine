from urllib import request

from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User


class LoginView(View):
    def post(self, request):
        if request.method == 'POST':
         
         username = request.POST.get('username')
         password = request.POST.get('password')

         authenticated_user = authenticate(request, username=username, password=password)

         if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('/recomend/home/')
            
         
         return render(request, 'login.html')
   
    def get(self, request):
        return render(request, 'login.html')
    

class signupView(View):
    def post(self,request):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password') 

            new_user = User.objects.create_user(username=username,email=email,password=password)

            if new_user is not None:
                login(request, new_user)
                return redirect('/recomend/home/')
            

            
            
        return render(request,'signup.html')
    def get(self,request):
        return render(request,'signup.html')