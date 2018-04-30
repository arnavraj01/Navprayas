from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from posts.templates import posts
from django.template import loader
from django.http import HttpResponse
from posts.models import Post

# Create your views here.
def signup(request):
	if request.method == 'POST':
		if request.POST['password1']== request.POST['password2']:
			try:	
				user = User.objects.get(username = request.POST['username'])
				return render(request,'accounts/signup.html', {'error': 'User already exists.'})
			except User.DoesNotExist:			
				user = User.objects.create_user(request.POST['username'], '' , request.POST['password2'])
				login(request, user)
				#template = loader.get_template('posts/Home.html')
				posts = Post.objects.order_by('date')
				#context = { 'post' : posts }
				return render(request, 'posts/Home.html', { 'post' : posts })
		else:
			return render(request,'accounts/signup.html', {'error': 'Passwords did not match!'})

	if request.method == 'GET':
		return render(request,'accounts/signup.html')


def loginUser(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])

		if user is not None:
			login(request,user)

			if 'next' in request.POST:
				return redirect(request.POST['next'])

			posts = Post.objects.order_by('date')
			#context = { 'post' : posts }
			return render(request, 'posts/Home.html', { 'post' : posts })
		else:
			return render(request,'accounts/login.html', {'error': 'User and password doesnt match'})
	if request.method == 'GET':
		return render(request,'accounts/login.html')