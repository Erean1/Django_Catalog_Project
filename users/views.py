from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from .forms import RegisterUserForm,LoginUserForm
from django.views.generic.edit import CreateView
from django.contrib.auth import login,logout,authenticate

from django.contrib import messages

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,"Register is Succesfully! Please Login")
        return response

    def form_invalid(self, form):
        messages.error(self.request,'An error occurred during registration. Please check your information.')
        return super().form_invalid(form)

# def register_user_view(request):
#     if request.method == "POST":
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Register is SuccesFully! Please Login")
#             return redirect('users:login')
#         else:
#             messages.error(request,'An error occurred during registration. Please check your information')
#     else:
#         form = RegisterUserForm()

#     return render(request,'users/register.html',{'form' : form})



class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        
        messages.success(self.request,"Login Succesfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):

        messages.error(self.request, 'Invalid Username or Password')
        return super().form_invalid(form)
    

# def login_user_view(request):
#     if request.method == "POST":
#         form = LoginUserForm(request.POST)

#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')

#             user = authenticate(request,username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 messages.success(request,"Login Succesfully!")
#                 return redirect('core:home')
#             else:
#                 messages.error(request,"Invalid Username or Password")
#                 return redirect('users:login')
#     else:
#         form = LoginUserForm()

#     return render(request,'users/login.html',{'form' : form})



class LogoutUserView(LogoutView):
    next_page = reverse_lazy('core:home')


# def logout_user_view(request):
#     logout(request)
#     return redirect('core:home')