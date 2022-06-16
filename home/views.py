from django.shortcuts import render,redirect,HttpResponseRedirect




from home.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    
    return render(request, 'index.html')





def user_login(request):
    if request.method == 'POST':
        
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)
       if user is not None:
        login(request, user)
		
        # Redirect to a success page.
        messages.success(request,'Login successfull !.')
        return render(request,'index.html')
       else:
        # Return an 'invalid login' error message.
        messages.success(request,'invalid user name & password !.')
        redirect('/login')

    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=User.objects.create_user(username, email, password)

        messages.success(request,'Account Created')
      
    return render(request,'signup.html')












