#Import necessary functions and classes from the hitcount module
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

#Function to update the view count for an object
def update_views(request, object):
    context = {} #Initialize empty context
    hit_count = get_hitcount_model().objects.get_for_object(object) #Get or create the hit count object for the given object
    hits = hit_count.hits #Retrieve the current number of hits (Views)
    hitcontext = context["hitcount"] = {"pk": hit_count.pk} #Store the hit count primary key in the context
    hit_count_response = HitCountMixin.hit_count(request, hit_count) #Update the hit count using the HitCountMixin

    #Check if the hit was counted
    if hit_count_response.hit_counted:
        hits = hits+1 #Increment the hit count
        hitcontext["hitcounted"] = hit_count_response.hit_counted #Add hit counted status to the context
        hitcontext["hit_message"] = hit_count_response.hit_message #Add hit message to the context
        hitcontext["total_hits"] = hits #Add the total hits to the context