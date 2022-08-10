
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from .models import *
from django.views.decorators.csrf import csrf_exempt

from .word_game import word_api


@login_required
def reviews(request):
    user = User.objects.get(pk=request.user.id)
    words = Review.objects.filter(user=user, archived=False).order_by('-updated_at')
    p = Paginator(words,8)
    pg_objects=[]
    for i in p.page_range:
        pg_objects.append(p.page(i))

    return render(request,'quiz/reviews.html',{'words':words,'pg_objects': pg_objects})

# referred to
# https://stackoverflow.com/questions/3090302/how-do-i-get-the-object-if-it-exists-or-none-if-it-does-not-exist-in-django#:~:text=Add%20a%20comment-,50,You%20can%20create%20a%20generic%20function%20for%20this.,-def%20get_or_none(

def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


@csrf_exempt
def quiz(request):
    # convert request body to list
    levels = json.loads(request.body)['selections']
    ls = word_api.get_wordlist(levels)
    return JsonResponse(ls,safe=False)

@csrf_exempt
def archive(request):
    word = json.loads(request.body)['word']
    user = User.objects.get(pk=request.user.id)
    r = Review.objects.get(user=user,word=word)
    r.archived= True
    r.save()
    return JsonResponse({'message':f'{word} was archived'})

@csrf_exempt
def review(request):
    if request.user.id:
       review_list = json.loads(request.body)['reviews']
       user = User.objects.get(pk=request.user.id)
       for word,definition in review_list:
          # user have the word on the dataset already
          if r :=get_or_none(Review, user=user, word=word):
             print('time plus 1')
             r.times+=1
             r.archived= False
             r.save()
          else:
             print('new word saved')
             r = Review(user=user,word=word,definition=definition)
             r.save() 
       return JsonResponse({'message':'words have been saved'})        
    return JsonResponse({'message':'Need to log in to save words to review'})

def index(request): 
    return render(request, "quiz/index.html")

def game(request):
    return render(request,'quiz/game.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("game"))
        else:
            return render(request, "quiz/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "quiz/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "quiz/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "quiz/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("game"))
    else:
        return render(request, "quiz/register.html")


