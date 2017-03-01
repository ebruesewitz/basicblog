from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.

# takes a request to render post list/homepage.
def post_list(request):
    # posts published on or before today, ordered with newest first.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # render page for all posts using format specified in html file
    return render(request, 'blog/post_list.html', {'posts': posts })

# takes request and pk for post to render the specific post on a page
def post_detail(request, pk):
    # either get and display the post or redirect to 404 not found page
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# takes request to display post creation form
def post_new(request):
    # submit button has been clicked to post content to blog
    if request.method == "POST":
        form = PostForm(request.POST)
        # assuming all fields in the form are filled in, save it and add a few extra details
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # after saving post to db, redirect user to page where they can view the post
            return redirect('post_detail', pk=post.pk)
    # Otherwise, show blank form for when the user first visits this page
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# takes a request to display the post creation/edit form with content from current post already in it.
def post_edit(request, pk):
    # either find the post or redirect to 404 page
    post = get_object_or_404(Post, pk=pk)
    # if the edit form has been submitted
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        # assuming the form is valid/all fields are filled in, save and add a few details to db
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #redirect to the page where you can view post.
            return redirect('post_detail', pk=post.pk)
    else:
        #otherwise, return the form with info already filled out.
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
