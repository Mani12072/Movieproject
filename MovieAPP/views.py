from django.shortcuts import render
from MovieAPP.forms import MoviesForm
from MovieAPP.models import Movies

#Create your views here.
def index_view(request):
    return render(request,'MovieApp/index.html')

def add_movie_view(request):
    formObj=MoviesForm()
    if request.method=="POST":
        formObj=MoviesForm(request.POST)
        if formObj.is_valid():
            print(formObj.cleaned_data['releasedate'])
            print(formObj.cleaned_data['moviename'])
            print(formObj.cleaned_data['actress'])
            print(formObj.cleaned_data['rating'])
            formObj.save()	#auto-commit
            return index_view(request)
    return render(request, 'MovieApp/addmovie.html',{'form1':formObj})

def list_movie_view(request):
    movies_list=Movies.objects.all().order_by('-rating') #(-)desc-order
    return render(request,'MovieApp/listmovie.html',{'movies_list':movies_list})


def f1(request):
    return render(request, 'MyApps1/child.html');
def f2(request):
    return render(request, "MyApps1/child2.html")