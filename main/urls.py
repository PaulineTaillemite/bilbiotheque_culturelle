from django.urls import path
from . import views


urlpatterns=[
    path("",views.test, name="test"),
    path("test2",views.test2, name="test2"),
    path("myprofile/",views.myprofile),
    
    path("test3/<studioname>",views.test3,name="test3" )

]