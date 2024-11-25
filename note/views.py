from django.shortcuts import HttpResponse,render,redirect
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def logout(request):
    return render(request,'logout.html')

def home(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'home.html',{'tweets':tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')
        else:
            form = TweetForm()
            return render(request, "tweet_form.html",{'form': form})
    else:
        # Handle GET request
        form = TweetForm()
        return render(request, "tweet_form.html", {'form': form})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')
        else:
            form = TweetForm(instance=tweet)
            return render(request, "tweet_form.html",{'form': form})
    else:
        # Handle GET request
        form = TweetForm(instance=tweet)
        return render(request, "tweet_form.html", {'form': form})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet,id=tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('home')
    return render(request, 'tweet_delete.html', {'tweet': tweet})

def register(request):
    if request.method =="POST":
        username=request.POST.get("username",None)
        email=request.POST.get("email",None)
        # mobile=request.POST.get("mobile",None)
        password=request.POST.get("password",None)

        user = User.objects.create_user(username=email,email=email,password=password)
        return render(request, "login.html")
    return render(request,"register.html")

def login(request):
   if request.method == "POST":
       username=request.POST.get("username")
       password=request.POST.get("password")

       user=authenticate(request,**{"username":username,"password":password})
       print(user)
       if not user:
           print("user not fount,please register")
       else:
           print("user found, logged in")
           auth_login(request,user)
           print(request.user)
           
       return redirect('tweet_create')

   return render(request,"login.html")