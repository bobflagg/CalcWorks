from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from work.models import Category, Sample
from django.template import RequestContext 

def sort_by_date(x):
    return x.created

def sample_list(request):
    """ 
    Lists all works samples starting with the most recent.
    """
    samples = Sample.objects.all().order_by('-created')
    front_page = []
    for x in samples:
        front_page.append(x)
    
    front_page.sort(key=sort_by_date, reverse=1)
    paginator = Paginator(front_page, 5)
    page = int(request.GET.get('page', '1'))
    samples = paginator.page(page)
    ROOT_URL = settings.ROOT_BLOG_URL
    ROOT_URL = ROOT_URL.rstrip("/")
    
    categories = Category.objects.all()

    return render_to_response(
        "work/sample_list.html", 
        {
            'samples': samples, 'ROOT_URL': ROOT_URL, 
            'subheading':'Work Samples'
        }, 
        context_instance=RequestContext(request))

def sample_detail(request, slug):
    """
    Takes the slug of a work sample, and displays that sample.
    """
    samples = get_object_or_404(Sample, slug=slug)
    ROOT_URL = settings.ROOT_BLOG_URL
    ROOT_URL = ROOT_URL.rstrip("/")
    return render_to_response(
        "work/sample_detail.html", 
        {
            'samples': samples, 'ROOT_URL': ROOT_URL, 
            'subheading':'Work Samples'
        }, 
        context_instance=RequestContext(request))
