from django.urls import path,include
from . import views,equ_views,other_view

urlpatterns = [
    # path('addtest/',views.addtest),
    path('stuman/', views.stuman),
    path('adminman/', views.adminman),
    path('adel/', views.adel),
    path('adch/', views.adch),
    path('adsearch/', views.adsearch),
    path('addadmin/', views.addadmin),

    path('stuch/', views.stuch),
    path('studel/', views.studel),
    path('addstu/', views.addstu),
    path('stusearch/', views.stusearch),

    path('equinfo/', equ_views.equinfo),
    path('equmansearch/', equ_views.equmansearch),
    path('equinfosearch/', equ_views.equinfosearch),
    path('equinfodel/', equ_views.equinfodel),
    path('equinfoch/', equ_views.equinfoch),
    path('addequinfo/', equ_views.addequinfo),

    path('equman/', equ_views.equman),
    # path('equmanote/', equ_views.equmanote),
    path('equmandel/', equ_views.equmandel),
    path('equmanbeizhu/', equ_views.equmanbeizhu),
    path('mansearch/', equ_views.mansearch),


    path('badequ/', equ_views.badequ),
    path('badequdel/', equ_views.badequdel),
    path('badsearch/', equ_views.badsearch),

    path('remindman/', other_view.remindman),
    path('remindch/', other_view.remindch),
    path('remindel/', other_view.remindel),
    path('addremind/', other_view.addremind),
    path('remindsearch/', other_view.remindsearch),


    path('recent/', other_view.recent),
    path('recentdel/', other_view.recentdel),
    path('recentsearch/', other_view.recentsearch),







]