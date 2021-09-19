from django.urls import path
from . import views
urlpatterns = [
    path('firstpg', views.firstpg, name='firstpg'),
    path('logintodo', views.logintodo, name='logintodo'),
    path('signout', views.signout, name='signout'),
    path('login2', views.login2, name='login2'),
    path('hometodo', views.hometodo, name='hometodo'),
    
    path('craccount', views.craccount, name='craccount'),
    path('goals', views.goals, name='goals'),
    path('lists', views.lists, name='lists'),
    path('delete/<int:dltitmid>', views.delete, name='delete'),
    path('delnotes/<int:noteid>', views.delnotes, name='delnotes'),
    path('dltitm/<int:dltid>', views.dltitm, name='dltitm'),
    path('deleteacc', views.deleteacc, name='deleteacc'),
    path('notes',views.notes, name='notes'),
    path('notes2',views.notes2, name='notes2'),
    
    path('diet', views.diet, name='diet'),
    path('diet2', views.diet2, name='diet2'),
    path('diet3', views.diet3, name='diet3'),
    path('plan', views.plan, name='plan'),
    path('plan2', views.plan2, name='plan2'),
    path('snacks', views.snacks, name='snacks'),
    path('water', views.water, name='water'),
    path('day2',views.day2, name='day2'),
    path('day3',views.day3, name='day3'),
    path('updatetask/<int:itmid>', views.updatetask, name='updatetask'),
    path('pendinglist', views.pendinglist, name='pendinglist'),
    path('profile', views.profile, name='profile'),
    path('today', views.today, name='today'),
    #path('dietajax', views.dietajax, name='dietajax'),
    path('food', views.food, name='food'),
    path('lunch', views.lunch, name='lunch'),
    path('dinner', views.dinner, name='dinner'),
    
]   