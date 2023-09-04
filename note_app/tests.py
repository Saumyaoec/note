from django.test import TestCase
from rest_framework.test import APIClient
from .models import Note

class NoteAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.note = Note.objects.create(noteId='1',title='Test Note', content='This is a test note.')

    def test_list_notes(self):
    	response = self.client.get('/notes/')  
    	self.assertEqual(response.status_code, 200)

    def test_create_note(self):
    	data = {'noteId':'11','title': 'New Note', 'content': 'This is a new note.'}
	    response = self.client.post('/notes/', data, format='json') 
	    self.assertEqual(response.status_code, 201)
	   
    def test_update_note(self):
        data = {'noteId':'111','title': 'Updated Note', 'content': 'This is an updated note.'}
        response = self.client.put(f'/notes/{self.note.id}/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_delete_note(self):
        response = self.client.delete(f'/notes/{self.note.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
