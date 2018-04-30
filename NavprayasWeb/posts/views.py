from django.shortcuts import render , get_object_or_404

# Create your views here.

from .models import Post
from django.contrib.auth.decorators import login_required

def home(request):
	posts = Post.objects.order_by('-date')
	return render(request, 'posts/Home.html' , {'posts':posts})

def post_details(request, post_id):
	# post = Post.objects.get(pk=post_id)
	post = get_object_or_404(Post,pk=post_id)
	return render(request, 'posts/PostDetails.html', {'post_id': post_id, 'post':post})

@login_required
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['image'] and request.POST['pub_date'] and request.POST['description']:
			post = Post()
			post.title = request.POST['title']
			post.image = request.POST['image']
			post.date = request.POST['pub_date']
			post.desc = request.POST['description']
			post.author = request.user
			post.save()
			render(request, 'posts/create.html', {'error': 'Post Saved!!!'})

		else:
			render(request, 'posts/create.html', {'error': 'ERROR : Please Fill all the fields.'})

	return render(request, 'posts/create.html')