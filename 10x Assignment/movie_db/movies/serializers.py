from rest_framework import serializers
from .models import Movie, Actor, Director, Technician, Genre

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    technicians = TechnicianSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        genres_data = validated_data.pop('genres')
        actors_data = validated_data.pop('actors')
        directors_data = validated_data.pop('directors')
        technicians_data = validated_data.pop('technicians')
        
        movie = Movie.objects.create(**validated_data)
        for genre_data in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            movie.genres.add(genre)
        for actor_data in actors_data:
            actor, _ = Actor.objects.get_or_create(**actor_data)
            movie.actors.add(actor)
        for director_data in directors_data:
            director, _ = Director.objects.get_or_create(**director_data)
            movie.directors.add(director)
        for technician_data in technicians_data:
            technician, _ = Technician.objects.get_or_create(**technician_data)
            movie.technicians.add(technician)
        
        return movie
