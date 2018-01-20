from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(editable=False,allow_unicode=True,unique=True)
    description = models.TextField(blank=True)
    description_html = models.TextField(editable=False,blank=True)
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    user = models.ForeignKey(User,related_name='membership')
    group = models.ForeignKey(Group,related_name='user_groups')

    def __str__(self):
        return self.user.username
    class Meta:
        unique_together = ['user','group']
