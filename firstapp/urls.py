from django.contrib import admin
from django.urls import path
from firstapp import views  # You wrote 'firstapp' bcz ur app name is 'firstapp'

urlpatterns = [
    path("",views.index,name='firstapp'),    # When the user comes from 'urls.py' of 'firstpro' and it see that the path of user 
                                            # this path, so it directs user to 'index' function of 'views' file 
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("experience/projects",views.projects,name='projects'),
    path("experience/internship",views.internship,name='internship'),
]