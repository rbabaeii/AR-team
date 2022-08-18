from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page.as_view() , name='home_page'),
    path('developers/' , views.Anytwo.as_view() , name = 'anytwo'),
    path('developers/rezababaei' , views.Reza.as_view() , name="reza"),
    path('developers/amirdavari/' , views.Amir.as_view() , name="amir"),
    path('developers/reza/madrak/' , views.Madrak_R.as_view() , name='madrak_r'),
    # path('projects/' , views.Project.as_view() , name= 'project'),
    path('developers/amir/madrak/' , views.Madrak_A.as_view() , name='ma')
]
