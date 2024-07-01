#Import the Post model from the main app
from main.models import Post

#Define search function
def searchFunction(request):
    search_context = {}  #Initialize an empty dictionary for the search context
    posts = Post.objects.all()  #Retrieve all posts from the database
    if "search" in request.GET:  #Check if the "search" parameter is in the GET request
        query = request.GET.get("q")  #Get the search query from the GET request
        #Filter logic starts here
        search_box = request.GET.get("search-box")  #Get the value of the "search-box" from the GET request
        if search_box == "Descriptions":
            objects = posts.filter(content__icontains=query)  #Filter posts by content if "search-box" is "Descriptions"
        else:
            objects = posts.filter(title__icontains=query)  #Otherwise, filter posts by title
        #Filter logic ends here
        search_context = {
            "objects": objects,  #Add the filtered posts to the search context
            "query": query,  #Add the search query to the search context
        }
    return search_context  #Return the search context
