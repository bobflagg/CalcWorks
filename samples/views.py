# Create your views here.
from django.http import HttpResponse
from django.template import Context, RequestContext
from django.template.loader import get_template

def main(request):
    template = get_template('main.html')
    variables = Context({
        'head_title': 'CalcWorks: Machine Learning Samples',
        'page_title': 'Machine Learning Samples',
        'page_body': 'here are some samples...'
    })
    output = template.render(variables)
    return HttpResponse(output)

def sample(request, sample_name):
    template = get_template('%s.html' % sample_name)
    variables = RequestContext(request, {'sample_%s' % sample_name:'1'})
    output = template.render(variables)
    return HttpResponse(output)
