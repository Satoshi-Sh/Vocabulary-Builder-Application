from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('game',views.game,name='game'),
    path('quiz',views.quiz,name='quiz'),
    path('review',views.review, name='review'),
    path('reviews',views.reviews,name='reviews'),
    path('archive',views.archive,name='archive')
]