#Import necessary modules from Django and other libraries
from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Category, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


#Homepage view
def home(request):
    forums = Category.objects.all() #Get all Categories
    num_posts = Post.objects.all().count() #Count all Posts
    num_users = User.objects.all().count() #Count all Users
    num_categories = forums.count() #Count all Categories
    try:
        last_post = Post.objects.latest("date") #Get latest Post
    except:
        last_post = [] #If no Posts, set last Posts as an empty list

    #Context to be passed to the template
    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories,
        "last_post":last_post,
        "title": "COSPLAY Forum"
    }
    return render(request, "forums.html", context) #Render the homepage with the context

#Post detailed view
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug) #Get the Post slug or return 404
    if request.user.is_authenticated:
        author = Author.objects.get(user=request.user) #Get the Author for the authenticated User
    
    if "comment-form" in request.POST:
        comment = request.POST.get("comment") #Get the Comment from the form
        new_comment, created = Comment.objects.get_or_create(user=author, content=comment) #Create new Comment
        post.comments.add(new_comment.id) #Add Comment to the Post

    if "reply-form" in request.POST:
        reply = request.POST.get("reply") #Get the Reply from the form
        comment_id = request.POST.get("comment-id") #Get the Comment ID to reply to
        comment_obj = Comment.objects.get(id=comment_id) #Get the COmment object
        new_reply, created = Reply.objects.get_or_create(user=author, content=reply) #Create new Reply
        comment_obj.replies.add(new_reply.id) #Add Reply to Comment


    #Context to be passed to the template
    context = {
        "post":post,
        "title": "COSPLAY "+post.title,
    }
    update_views(request, post) #Update view count for the Post

    return render(request, "detail.html", context) #Render the detailed view with the context

#Posts view
def posts(request, slug):
    category = get_object_or_404(Category, slug=slug) #Get the Category by slug or return 404
    posts = Post.objects.filter(approved=True, categories=category) #Get only approved Posts in the Category
    paginator = Paginator(posts, 5) #Paginate Posts, 5 per page
    page = request.GET.get('page') #Get the current page number
    try:
        posts = paginator.page(page) #Get the Posts for the current page
    except PageNotAnInteger:
        posts = paginator.page(1) #If page is not an integer, deliver the first page
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  #If page is out of range, deliver the last page

    #Context to be passed to the template
    context = {
        "posts": posts,
        "forum": category,
        "title": "COSPLAY: Posts"
    }

    return render(request, "posts.html", context) #Render the Posts view with the context

#Login requirements
@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None, request.FILES or None) #Create a new Post form
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = Author.objects.get(user=request.user) #Get the Author from the authenticated User
            new_post = form.save(commit=False) #Save the form data to a new Post object, without committing to the database
            new_post.user = author #Set the Post's Author
            new_post.approved = True #Set the post as NOT approved(Auto-approve)
            new_post.save() #Save the new Post to the database
            form.save_m2m() #Save the many-to-many data for the form
            return redirect("home") #Redirect to Homepage
    context.update({
        "form": form,
        "title": "COSPLAY: Create New Post"
    })
    return render(request, "create_post.html", context) #Render the create Post view with the context

#Latest posts view
def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10] #Get the 10 latest approved Posts
    context = {
        "posts":posts,
        "title": "COSPLAY: Latest 10 Posts"
    }

    return render(request, "latest-posts.html", context) #Render the latest Posts view with the context

#Search posts
def search_result(request):

    return render(request, "search.html") #Render the search results view (Currently empty)