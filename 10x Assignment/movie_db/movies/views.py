from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        actor_id = self.request.query_params.get('actor')
        director_id = self.request.query_params.get('director')
        if actor_id:
            queryset = queryset.filter(actors__id=actor_id)
        if director_id:
            queryset = queryset.filter(directors__id=director_id)
        return queryset

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @action(detail=True, methods=['post'])
    def delete_if_not_in_use(self, request, pk=None):
        actor = self.get_object()
        if not Movie.objects.filter(actors=actor).exists():
            actor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Actor is associated with movies and cannot be deleted."}, status=status.HTTP_400_BAD_REQUEST)
