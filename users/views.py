from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.views import View
from django.views import generic
from django.contrib.auth.views import LoginView


from .forms import LoginForm, SignUpForm, ProfilePicForm
from .models import Image

USER = get_user_model()


# class Create(CreateView):
#     form_class = SignUpForm
#     template_name = 'users/signup.html'
#     success_url = '/users/profile/'

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = USER(
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.save()
            user.set_password(form.cleaned_data['password1'])
            user.save()

            subject = "Please verify your email"
            message = "Please verify your email by clicking on the following link : "
            from_email = 'admin@admin.com'
            recipients = [user.email,]
            html_message ='<p><a href="http://127.0.0.1:8000/users/login/">Click to validate email</a></p>'
            send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipients,html_message=html_message)

            return HttpResponse("An email has been sent to you. Please confirm your email to complete your registration.")
    
    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(email=form.cleaned_data['email'],
            password=form.cleaned_data['password'])
            print(form.cleaned_data)

            if user:
                print("user found",user)
                login(request,user)
                return redirect('/users/profile/')
    
    elif request.method=='GET':
        if request.user.is_authenticated:
            return redirect('/users/profile/')
        form = LoginForm()
    
    return render(request, 'users/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('/users/login/')

@login_required()
def profile_view(request):
    images = Image.objects.all()
    return render(request,'users/profile.html',{'images':images})    


def upload_pic(request):
    if request.method == 'POST':
        form = ProfilePicForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/users/profile/')
    else:
        form = ProfilePicForm()
    return render(request, 'users/upload_pic.html',{'form':form})

# class Detail(DetailView):
#     model = USER
#     template_name = 'users/profile.html'
#     pk_url_kwarg = 'id'
#     context_object_name = 'user_obj'