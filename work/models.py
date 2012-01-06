import datetime
from tagging.fields import TagField
from tagging.models import Tag
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink


VIEWABLE_STATUS = [3, 4]

class ViewableManager(models.Manager):
    def get_query_set(self):
        default_queryset = super(ViewableManager, self).get_query_set()
        return default_queryset.filter(status__in=VIEWABLE_STATUS)

class Category(models.Model):
    """
    Categories for work samples.
    """
    label = models.CharField(blank=True, max_length=50)
    slug = models.SlugField()

    class Meta:
        ordering = ['label']
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.label
  
    @permalink
    def get_absolute_url(self):
        return ("work-category", (), {'slug' : self.slug})

class Sample(models.Model):
    """
    A sample of work.
    """

    STATUS_CHOICES = (
        (1, "Needs Edit"),
        (2, "Needs Approval"),
        (3, "Published"),
        (4, "Archived"),
    )

    title = models.CharField(max_length=80)
    slug = models.SlugField()
    category = models.ManyToManyField(Category)
    body = models.TextField()
    owner = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)
    tags = TagField()

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self) 

    class Meta:
        ordering = ['-modified']
        verbose_name_plural = "Work Samples"

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ("work-sample", (), {'slug' : self.slug})

    admin_objects = models.Manager()
    objects = ViewableManager()
