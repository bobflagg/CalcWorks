from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext 

def about(request):
    """ 
        Displays some general information about the site and about me.
    """
    ROOT_URL = settings.ROOT_BLOG_URL
    ROOT_URL = ROOT_URL.rstrip("/")
    return render_to_response("about.html", {'ROOT_URL': ROOT_URL, 'heading':'About Me'}, context_instance=RequestContext(request))

def contact(request):
    """ 
        Displays some contact information.
    """
    ROOT_URL = settings.ROOT_BLOG_URL
    ROOT_URL = ROOT_URL.rstrip("/")
    return render_to_response("contact.html", {'ROOT_URL': ROOT_URL, 'heading':'Contact Information'}, context_instance=RequestContext(request))
