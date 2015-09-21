from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from bookmark_app.models import Bookmark

def home(request):
	# displays home page
	return render(request, 'bookmark_app/home.html', {})

def bookmarks(request):
	# displays list of urls:description
	#retrieves all bm in db
	bookmarks = Bookmark.objects.all()
	# if user searchs URL or description, execute this
	if request.GET.get('search'):
		search = request.GET.get('search')
		bookmarks = Bookmark.objects.filter(Q(URL__icontains=search) | Q(Description__icontains=search))

	return render(request, 'bookmark_app/bookmarks.html', {'bookmarks':bookmarks})

def new(request):
	# user input url/desription
	return render(request, 'bookmark_app/new.html', {})

def create(request):
	# gets user input, saves to db
	#creates new instance of Bookmark
	bookmark = Bookmark(URL = request.POST.get("url"), Description = request.POST.get("description"))
	bookmark.save()
	return redirect('bookmarks')

def update(request,bm_id):
	# allows user to update url or description
	#get the bookmark
	bookmark = Bookmark.objects.get(pk=bm_id)
	return render(request, 'bookmark_app/update.html', {'url':bookmark.URL, 'description':bookmark.Description, 'id':bm_id})

def update_url(request,bm_id):
	# updates the user's URL
	#get the bookmark
	bookmark = Bookmark.objects.get(pk=bm_id)
	# update instance of Bookmark
	bookmark.URL = request.POST.get("url")
	bookmark.save()
	return redirect('bookmarks')


def update_desc(request,bm_id):
	# updates the user's description
	#get the bookmark
	bookmark = Bookmark.objects.get(pk=bm_id)
	# update instance of Bookmark
	bookmark.Description = request.POST.get("description")
	bookmark.save()
	return redirect('bookmarks')

def remove(request,bm_id):
	# removes bm when button is clicked
	#get the bookmark
	bookmark = Bookmark.objects.get(pk=bm_id)
	#delete it
	bookmark.delete()
	return redirect('bookmarks')
