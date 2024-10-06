from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from api.serializers import MovieSerialzer,ActorSerializer,AlbumSerializer,TrackSerializer,ReviewSerializer

from rest_framework import viewsets

from myapp.models import Movies,Actor,Album,Tracks

from rest_framework.decorators import action

class MovieListCreateView(APIView):

    def get(self,request,*args, **kwargs):

        # logic for returning all movies

        qs=Movies.objects.all()

        serializer_instance=MovieSerialzer(qs,many=True) #serialization

        return Response (data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):

        serializer_instance= MovieSerialzer(data=request.data) #deserialization

        if serializer_instance.is_valid():

            serializer_instance.save()

         # logic for adding movie

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
    

class MovieRetrieveUpdateDestroyView(APIView):    

    def get(self,request,*args,**kwargs):

        #extract id from url and return moviedetail with movieid=id
        id=kwargs.get("pk")

        movie_obj=Movies.objects.get(id=id) 

        serializer_instance=MovieSerialzer(movie_obj,many=False)

        return Response(data=serializer_instance.data)

    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        #extract movie id and update movie detail

        movie_obj=Movies.objects.get(id=id) 

        serializer_instance=MovieSerialzer(data=request.data,instance=movie_obj)
        
        if serializer_instance.is_valid():

            serializer_instance.save()

         # logic for adding movie

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        

    def delete(self,request,*args,**kwargs):


        id=kwargs.get("pk")

        #extract id from url and delete movie with movieid=id

        Movies.objects.get(id=id).delete() 

        return Response(data={"message":"deleted"})
    
    
class LanguagesView(APIView):  


    def get(self,request,*args,**kwargs):

        qs=Movies.objects.all().values_list("language",flat=True).distinct() 

        return Response(data=qs)

    
class GenresView(APIView):  


    def get(self,request,*args,**kwargs):

        qs=Movies.objects.all().values_list("genre",flat=True).distinct() 

        return Response(data=qs)    
    


class ActorViewSet(viewsets.ViewSet):

    def list(self,request,*args,**kwargs):

        qs=Actor.objects.all()

        serializer_instance=ActorSerializer(qs,many=True)# serialization

        return Response(data=serializer_instance.data)

    def create(self,request,*args,**kwargs):

        serializer_instance=ActorSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        else:

            return Response(data=serializer_instance.errors)

    def retrieve(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        serializer_instance=ActorSerializer(actor_obj,many=False)

        return Response(data=serializer_instance.data)


    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        serializer_instance=ActorSerializer(data=request.data,instance=actor_obj)

       
        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)
        

    def destroy(self,request,*args, ** kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        actor_obj.delete() 

        return Response(data={"messege":"delete"})


class AlbumViewSetView(viewsets.ModelViewSet):

    serializer_class=AlbumSerializer

    queryset=Album.objects.all()


    @action(methods=["GET"],detail=False)
    def languages (self, request, *args, ** kwargs) :

        qs=Album.objects.all().values_list("language", flat=True).distinct()

        return Response(data=qs)
    

    @action(methods=["GET"],detail=False)
    def directors (self, request, *args, ** kwargs) :

        qs=Album.objects.all().values_list("director", flat=True).distinct()

        return Response(data=qs)
    

    @action(methods=["POST"],detail=True)
    def add_review(self, request, *args, ** kwargs):

        id=kwargs.get("pk")

        album_obj=Album.objects.get(id=id)

        serializer_instance=ReviewSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(album_object=album_obj)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
    

    @action(methods=["POST"],detail=True)
    def add_track(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_obj=Album.objects.get(id=id)

        serializer_instance=TrackSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(album_object=album_obj)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)


class TrackViewSetView(viewsets.ModelViewSet):

    serializer_class=TrackSerializer

    queryset=Tracks.objects.all()        

