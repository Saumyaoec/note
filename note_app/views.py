from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import filters

class NoteCreate(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class NoteUpdate(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'noteId'

    def get_object(self):
        note_id = self.kwargs.get('noteId')
        try:
            obj = Note.objects.get(noteId=note_id)
            return obj
        except Note.DoesNotExist:
            logging.error(f"Note with noteId {note_id} does not exist.")
            raise

class NoteList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['createdAt', 'updatedAt']

class NoteDetail(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'noteId'

class NoteDelete(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'noteId'