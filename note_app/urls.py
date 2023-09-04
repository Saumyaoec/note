from django.urls import path
from .views import NoteCreate,NoteUpdate,NoteList,NoteDetail,NoteDelete

urlpatterns = [
    path('note_create/', NoteCreate.as_view(), name='note-create'),
    path('notes_update/<int:noteId>/', NoteUpdate.as_view(), name='note-update'),
    path('note_list/', NoteList.as_view(), name='note-list'),
    path('note_detail/<int:noteId>/', NoteDetail.as_view(), name='note-detail'),
    path('note_delete/<int:noteId>/', NoteDelete.as_view(), name='note-delete'),


]
