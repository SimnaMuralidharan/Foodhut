from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index),
    path('reg/',registration),
    path('log/',login),
    path('regis/',regis),
    path('verify/<auth_token>',verify),
    path('login/',userlogin),
    path('nonupload/',nfile),
    path('vegupload/',vfile),
    path('restdisplay/',nondisplay),
    path('vegdisplay/',vegdisplay),
    path('veg_edit/<int:id>',vegedit),
    path('vegdelete/<int:id>',vegdelete),
    path('nonedit/<int:id>',nonvegedit),
    path('nonvegdelete/<int:id>',nonvegdelete),
    path('adddetails/',add_details),
    path('contactdisplay/',contactdisplay),
    path('displayedit/<int:id>',displayedit),
    path('userprofile/',userprofile)


]