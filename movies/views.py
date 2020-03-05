from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
import http.client
from .models import *
import json
import collections

# Create your views here.
def movie_detail(request,pk):

    a = get_object_or_404(movie, pk=pk)
    


    api='55e142e9c2c6c33fbf1e57af703ddf4e'


    #https://api.themoviedb.org/4/list/{list_id}?page=1&api_key=<<api_key>>

    #a=https://api.themoviedb.org/4/list/{list_id}?page=1&api_key=<<api_key>>

    conn = http.client.HTTPSConnection("api.themoviedb.org")
    s=454626    
    conn.request("GET", "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(s,api))

    res = conn.getresponse()
    data = res.read()

    new=data.decode("utf-8")
    resp_dict = json.loads(new)
    myStuff = movie.objects.all()
    
    
    #for i in myStuff.categorys.all():
    #   print(i)


        
        

    return render(request,'movie_detail.html',{'a':a,'myStuff':myStuff})



def populate_movie(request):

    #Adding Genres

    conn = http.client.HTTPSConnection("api.themoviedb.org")
    conn.request("GET", "https://api.themoviedb.org/3/genre/movie/list?api_key=55e142e9c2c6c33fbf1e57af703ddf4e&language=en-US")
    res = conn.getresponse()
    data = res.read()

    new=data.decode("utf-8")
    resp_dict = json.loads(new)
    

    for i in resp_dict['genres']:
        idss=i['id']
        nam=i['name']
    

        try:
            if category.objects.get(ids=idss):
                break
                return redirect("/")
            
                
        except Exception as e:
            print('ssssss')
        
        
        category.objects.create(ids=idss,name=nam)

    #adding latest movies
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    conn.request("GET", "https://api.themoviedb.org/3/movie/latest?api_key=55e142e9c2c6c33fbf1e57af703ddf4e&language=en-US")
    res = conn.getresponse()
    data = res.read()

    new=data.decode("utf-8")
    resp_dict = json.loads(new)

    m_id=resp_dict['id']
    m_name=resp_dict['original_title']
    m_lang=resp_dict['original_language']
    m_desc=resp_dict['overview']
    m_status=resp_dict['status']
    m_logo=resp_dict['poster_path']
    m_vote=resp_dict['vote_average']
    m_pop=resp_dict['popularity']
    m_gen=resp_dict['genres']
    
    #
    try:

    
        if movie.objects.get(movie_ids=m_id):
            print("already added")
        
    except Exception as e:
        movie.objects.create(movie_ids=m_id,movie_name=m_name,movie_lang=m_lang,movie_desc=m_desc,status=m_status,movie_logo=m_logo,movie_vote=m_vote,movie_pop=m_pop)
        if m_gen==[]:
            print('no genres')
        else:
            
            m_gens=resp_dict['genres']
            fs=get_object_or_404(category, ids=m_gens['id'])

            diego = movie.objects.get(movie_ids=m_id)
            diego.categorys.add(fs)
        print('Got error')





    #adding popular movies
    
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    conn.request("GET", "https://api.themoviedb.org/3/movie/popular?api_key=55e142e9c2c6c33fbf1e57af703ddf4e&language=en-US&page=1")
    res = conn.getresponse()
    data = res.read()

    new=data.decode("utf-8")
    resp_dicts = json.loads(new)

    print('fffdfdfdf')
    #print(resp_dicts['results'])


    for i in resp_dicts['results']:
        p_id=i['id']
        p_name=i['original_title']
        p_lang=i['original_language']
        p_desc=i['overview']
        #p_status=i['status']
        p_logo=i['poster_path']
        p_vote=i['vote_average']
        p_pop=i['popularity']


        p_gen=i['genre_ids']
        print(p_id)


        try:


    
            if movie.objects.get(movie_ids=p_id):
                print("already")
        
        except Exception as e:
            movie.objects.create(movie_ids=p_id,movie_name=p_name,movie_lang=p_lang,movie_desc=p_desc,status='released',movie_logo=p_logo,movie_vote=p_vote,movie_pop=p_pop)
        
            #movie.objects.create(movie_ids=p_id,movie_name=p_name,movie_lang=p_lang,movie_desc=p_desc,status='released',movie_logo=p_logo,movie_vote=p_vote,movie_pop=p_pop)

            print('Got error')

        for item in p_gen:
            ss=get_object_or_404(category, ids=item)
            diego = movie.objects.get(movie_ids=p_id)
            diego.categorys.add(ss)

            
    

    return redirect("/")


def home_page(request):
    pop=movie.objects.all()

    return render(request,'home.html',{'pop':pop})


def create_list(request):
    #pop=movie.objects.all()
    if request.method== 'POST':
        pro=request.POST['list_name']

        lists.objects.create(list_name=pro)

        return redirect("/create_list/list/")


    return render(request,'lists.html',{})


def create_list2(request):
    obj= lists.objects.latest('id')
    print(obj)
    pop=movie.objects.all()
    return render(request,'new_list.html',{'pop':pop,'obj':obj})



def select_movie(request,pk):
    obj= lists.objects.latest('id')
    a = get_object_or_404(movie, pk=pk)

    diego = lists.objects.get(list_name=obj)
    diego.list_movie.add(a)
    

    return redirect("/create_list/list/")


def view_list(request):
    get_list=lists.objects.all()
    return render(request,'view_list.html',{'get_list':get_list})



def recommend(request,pk):
    global get
    count=0
    li=[]
    myStuff = lists.objects.get(pk=pk)
    
        #print(i.id)
    #myStuff = lists.objects.get(id=i.id)
    for t in myStuff.list_movie.all():
        for s in t.categorys.all():
            a=s
            li.append(a)
    
    ss=collections.Counter(li).most_common(1)


    try:
        for i in ss:
            new=i[0]
        

            an=movie.objects.all()
            for i in an:
            
                get=movie.objects.filter(categorys=new)
    except Exception as e:
        print(e)
    




    

    #new_stuff=movie.objects.get(id=162)

    #for i in new_stuff.categorys.all():
    #    print(i)


    return render(request,'recommended.html',{'get':get})
