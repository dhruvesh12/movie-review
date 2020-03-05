from django.urls import path, include
from movies.views import *
#from movies import urls

urlpatterns = [
	path('',home_page, name='home_page'),
	path('movie/<int:pk>/',movie_detail,name='movie_detail'),
    path('add_movie/',populate_movie, name='populate_movie'),
    path('create_list/',create_list, name='create_list'),
    path('create_list/list/',create_list2, name='create_list2'),
    path('create_list/selected/<int:pk>/',select_movie, name='selected_movie'),
    path('list/',view_list, name='view_list'),
    path('list/suggested/<int:pk>/',recommend, name='recommend'),

    
]