from rest_framework import viewsets, permissions
from todolist.api.models import Todo
from todolist.api.serializers import TodoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        Todo.objects.filter(user=request.user).delete()
        return Response({"message": "Все задачи удалены"})

class TodoViewSet(viewsets.ModelViewSet):
    ...
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_completed']
    search_fields = ['title', 'description']

    