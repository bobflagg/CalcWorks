import feedparser
from work.models import Category, Sample
from django.conf import settings
from django import template

register = template.Library()

def parse_github():
    if settings.GITHUB_USERNAME:
        """ Grab latest commits from GitHub """
        d = feedparser.parse("http://github.com/%s.atom" % settings.GITHUB_USERNAME)
        e = d.entries[:5]
        commit = "<ul>"
        for x in e:
            link = x['link']
            link = link.lstrip("http://github.com/")
            link = "http://github.com/%s" % link
            commit += "<li>"
            commit += '<a href="%s">' % link
            commit += x['title_detail']['value']
            commit += "</a>\n@ %s" % x['updated']
            commit += "</li>"
        commit += "</ul>"
        return commit
    else:
        commit = False
        return commit

def worksidebar():
    sitename = settings.BLOG_NAME

    return {
        'sitename': sitename, 
        'categories': Category.objects.all(),
        'work_samples':Sample.objects.all().order_by('-created'), 
        'commit': parse_github(),
    }

register.inclusion_tag('work/sidebar.html')(worksidebar)
