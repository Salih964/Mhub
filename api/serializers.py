from rest_framework import serializers

from myapp.models import Movies,Actor,Album,Tracks,Review

class MovieSerialzer(serializers.ModelSerializer):

    class Meta:

        model=Movies

        fields="__all__"

class ActorSerializer(serializers.ModelSerializer):

    class Meta:

        model=Actor

        fields="__all__"




class TrackSerializer(serializers.ModelSerializer):

    album_object=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Tracks

        fields="__all__"

        read_only_fields= ["id","album_object"]    


class ReviewSerializer(serializers.ModelSerializer):

    album_object=serializers.StringRelatedField(read_only=True)
    
    class Meta:

        model=Review

        fields="__all__"

        read_only_fields=["id", "created_date", "album_object"]


class AlbumSerializer(serializers.ModelSerializer):

    songs=TrackSerializer(many=True,read_only=True) #nested serializer

    song_count=serializers.CharField(read_only=True)

    review_count=serializers.CharField(read_only=True)
    
    avg_rating=serializers.CharField(read_only=True)

    reviews=ReviewSerializer(many=True,read_only=True)


    class Meta:

        model=Album    

        fields=["id","title","year","language","director","song_count","review_count","avg_rating","songs","reviews"]

