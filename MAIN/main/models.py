#Import necessary modules from Django and other libraries
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
from django.shortcuts import reverse

#Fetch user model from system
User = get_user_model()

#Define Author model
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Link to user model
    fullname = models.CharField(max_length=40, blank=True) #Full name of the user/author
    slug = slug = models.SlugField(max_length=400, unique=True, blank=True) #URL version of the name
    bio = HTMLField() #HTML field for author's bio
    points = models.IntegerField(default=0) #Points the author has received
    profile_pic = ResizedImageField(size=[50, 80], quality=100, upload_to="authors", default=None, null=True, blank=True) #Profile image

    def __str__(self):
        return self.fullname #String representation of the model

    #Property to count the number of posts by the author
    @property
    def num_posts(self):
        return Post.objects.filter(user=self).count()
    

    #Save post method to generate slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

#Define Category model
class Category(models.Model):
    title = models.CharField(max_length=50) #Category title
    slug = models.SlugField(max_length=400, unique=True, blank=True) #URL version of the category
    description = models.TextField(default="description") #Description of the category

    class Meta:
        verbose_name_plural = "categories" #Plural name for Category
    def __str__(self):
        return self.title #String representation of the model
    

#Category save method to generate slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    #Method to get the URL of the category
    def get_url(self):
        return reverse("posts", kwargs={
            "slug":self.slug
        })

    #Property to count the number of posts in the category
    @property
    def num_posts(self):
        return Post.objects.filter(categories=self).count()
    
    #Property to get the latest post in the category
    @property
    def last_post(self):
        return Post.objects.filter(categories=self).latest("date")


#Define Reply model
class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE) #Link to Author model
    content = models.TextField() #Textfield for Reply content
    date = models.DateTimeField(auto_now_add=True) #Date reply was created

    def __str__(self):
        return self.content[:100] #String representation of the model (first 100 characters)

    class Meta:
        verbose_name_plural = "replies" #Plural name for the model


#Define Comment model
class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE) #Link to Author model
    content = models.TextField() #Textfield for Comment content
    date = models.DateTimeField(auto_now_add=True) #Date comment was created
    replies = models.ManyToManyField(Reply, blank=True) #Many-to-many relationship with Reply

    def __str__(self):
        return self.content[:100] #String representation of the model (first 100 characters)


#Define Post model
class Post(models.Model):
    title = models.CharField(max_length=400) #Title of the Post
    slug = models.SlugField(max_length=400, unique=True, blank=True) #URL version of the Post
    user = models.ForeignKey(Author, on_delete=models.CASCADE) #Link to Author model
    content = HTMLField() #HTML field for the Post's content
    image = models.ImageField(upload_to='post_images', blank=True, null=True) #Image upload function
    categories = models.ManyToManyField(Category) #Many-to-many relationship with Category
    date = models.DateTimeField(auto_now_add=True) #Date Post was created
    approved = models.BooleanField(default=False) #Post approved status (Default = False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    ) #Generic relation for Hitcount (Views)
    tags = TaggableManager() #Taggable manager for Tags
    comments = models.ManyToManyField(Comment, blank=True) #Many-to-many relationship with comments
    closed = models.BooleanField(default=False) #Open or closed status of the Post (Default = False)
    state = models.CharField(max_length=40, default="zero") #State of the Post
    
    #Post save method to generate slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title #String representation of the model

    #Method to get URL of the Post
    def get_url(self):
        return reverse("detail", kwargs={
            "slug":self.slug
        })

    #Property to count the number of comments on the post
    @property
    def num_comments(self):
        return self.comments.count()

    #Property to get the latest reply on the post
    @property
    def last_reply(self):
        return self.comments.latest("date")

    