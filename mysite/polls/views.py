from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, worrrld. You're at the polls index.")

class SongListView(CreateView):
	model = SongList
	form_class = SongListForm
	template_name = ''

# Create your views here.
