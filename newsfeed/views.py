from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from newsfeed.models import kicks
from newsfeed.models import users

# currentUser = ''
# GLOBAL_Entry = None


 
#@login_required(login_url='/login/')
#importing movies from the database    --Saksham

# the home view is for the landing page
def home(request):
		
	# entries = kicks.objects.all()[:10]
	entries = kicks.objects.all()
	
	return render_to_response('index.html', {'kicks' : entries})
	
# uncomment @login to lock user_profile for unauthorized access

#login view to load after signing in
def login_user(request):
	#global currentUser, GLOBAL_Entry
	
	
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
					#request.session['currentUser'] = user.username
				currentUser = user.username
				request.session["currentUser"] = currentUser
					#print(user.username)
					#return HttpResponse({user.username})
				return HttpResponseRedirect('/profile/')
				#return render_to_response('profile.html', context_instance=RequestContext(request))
	return render_to_response('index.html', context_instance=RequestContext(request))


#@login_required(login_url='/home/')
@login_required
def user_profile(request):
	#logout(request)
	#request.session["fav_color"] = "blue"
	
	users_temp = users.objects.all()
	#username1 = request.session.get('currentUser')
	#return HttpResponse({currentUser})
	return render_to_response('profile.html', {'users' : users_temp},context_instance=RequestContext(request))

@login_required
def friends(request):
		users_temp = users.objects.all()
		#username1 = request.session.get('currentUser')
		#return HttpResponse({currentUser})
		return render_to_response('friends.html', {'users' : users_temp},context_instance=RequestContext(request))

@login_required
def edit_profile_form(request):
    if request.method == 'POST':
    	getCurrentUser = request.POST.get('getCurrentUser','')
        firstName = request.POST.get('firstName','')
        lastName = request.POST.get('lastName','')
        email = request.POST.get('email','')
        expertise = request.POST.get('expertise','')
        genres = request.POST.get('genres','')
        ratings = request.POST.get('ratings','')
        top100 = request.POST.get('top100','')
        watchlist = request.POST.get('watchlist','')
        thumbnail = request.FILES.get('thumbnail','')
        
        edit_obj = users.objects.get(userName = getCurrentUser)
        edit_obj.firstName = firstName
        edit_obj.lastName = lastName
        edit_obj.email = email
        edit_obj.expertise = expertise
        edit_obj.genres = genres
        edit_obj.ratings = ratings
        edit_obj.top100 = top100
        edit_obj.watchlist = watchlist
        edit_obj.thumbnail = thumbnail
        edit_obj.save()
        users_temp = users.objects.all()
    return render_to_response('profile.html', {'users' : users_temp},context_instance=RequestContext(request))

@login_required
def friend_profile(request):
	#logout(request)
	if 'currentUser' not in request.session:
		return HttpResponseRedirect('/home/')
	else:
		users_temp = users.objects.all()
		if request.method == 'POST':
		    selectedFriend = request.POST.get('selectedFriend','')
		        
		    return render_to_response('friend_profile.html', {'users' : users_temp,'selectedFriend' : selectedFriend},context_instance=RequestContext(request))

@login_required        
def kicks_list(request):
	#logout(request)
	
	kicks_temp = kicks.objects.all().order_by("-id")
	
	return render_to_response('kicks.html', {'kicks' : kicks_temp},context_instance=RequestContext(request))     

@login_required
def add_kick_form(request):

    if request.method == 'POST':
    	kickTitle = request.POST.get('kickTitle','')
        releaseDate = request.POST.get('releaseDate','')
        category = request.POST.get('category','')
        directors = request.POST.get('directors','')
        writers = request.POST.get('writers','')
        stars = request.POST.get('stars','')
        ratings = request.POST.get('ratings','')
        links = request.POST.get('links','')
        poster = request.FILES.get('poster','')
        
        add_obj = kicks(

		        kickTitle = kickTitle,
		        releaseDate = releaseDate,
		        category = category,
		        directors = directors,
		        writers = writers,
		        stars = stars,
		        ratings = ratings,
		        links = links,
		        poster = poster
        )
        add_obj.save()
        kicks_temp = kicks.objects.all()
        
    return render_to_response('kicks.html', {'kicks' : kicks_temp},context_instance=RequestContext(request))   

@login_required
def kick_profile(request):
	
	
	kicks_temp = kicks.objects.all()
	if request.method == 'POST':
	    selectedKick = request.POST.get('selectedKick','')
	        
	return render_to_response('kick_profile.html', {'kicks' : kicks_temp,'selectedKick' : selectedKick},context_instance=RequestContext(request))

@login_required
def season(request):
	#logout(request)
	#request.session["fav_color"] = "blue"
	
	users_temp = users.objects.all()
	#username1 = request.session.get('currentUser')
	#return HttpResponse({currentUser})
	return render_to_response('season.html', {'users' : users_temp},context_instance=RequestContext(request))	
# Create your views here.
