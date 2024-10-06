from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from myapp.models import Movies

from myapp.forms import MovieForm,MovieModelForm

class MovieListView(View):

    def get(self,request,*args,**kwargs):

        qs=Movies.objects.all()

        return render(request,"movie_list.html",{"data":qs})
    

class MovieCreateView(View):

    def get(self,request,*args,**kwargs):

        # form_instance=MovieForm()

        form_instance=MovieModelForm()

        return render(request,"movie_add.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        # form_instance=MovieForm(request.POST)

        form_instance=MovieModelForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            # data=form_instance.cleaned_data

            # Movies.objects.create(**data)

            return redirect ("movie-list")
        else:
            return render(request,"movie-create",{"form":form_instance})    

class MovieDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id)

        return render(request,"movie_detail.html",{"data":qs})
    

class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Movies.objects.get(id=id).delete()

        return redirect("movie-list")

class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_object=Movies.objects.get(id=id)

        # dictionary={
        #     "title":movie_object.title,
        #     "year":movie_object.year,
        #     "director":movie_object.director,
        #     "run_time":movie_object.run_time,
        #     "language":movie_object.language,
        #     "genre":movie_object.genre,
        #     "producer":movie_object.producer
        # }

        # form_instance=MovieForm(initial=dictionary)

        form_instance=MovieModelForm(instance=movie_object)

        return render(request,"movie_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST) 

        id=kwargs.get("pk")

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Movies.objects.filter(id=id).update(**data)

            return redirect("movie-list")
        else:
            return render(request,"movie_edit.html",{"form":form_instance})

      

        