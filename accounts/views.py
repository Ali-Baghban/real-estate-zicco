from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from contact.models import Order
def dashboard(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = get_object_or_404(User,id=user_id)
        orders = Order.objects.filter(client_name=user.username).order_by('-contact_date')
        context = {'orders':orders,}
        return render(request, 'cp/dashboard.html', context=context)
    else:
        return redirect('index')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return redirect('index')
    else:
        return redirect('index')

def register(request):
    if request.method == "POST":
        email       = request.POST['email']
        username    = request.POST['username']
        password    = request.POST['password']
        repassword  = request.POST['repassword']
        if len(password) | len(repassword) < 8 :
            return redirect('index')
        else:
            if password != repassword:
                return redirect('index')
            else:
                if User.objects.filter(username=username).exists():
                    return redirect('index')
                else:
                    if User.objects.filter(email=email).exists():
                        return redirect('index')
                    else:
                        user = User.objects.create_user(username=username,email=email,password=password)
                        user.save()
                        user = auth.authenticate(username=username, password=password)
                        if user is not None:
                            auth.login(request,user)
                            return redirect('dashboard')

    else:
        return redirect('index')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('index')
    else:
        return redirect('index')


