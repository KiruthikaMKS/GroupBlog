from django.db import models
from django.core.urlresolvers import reverse
from groups.models import Group
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts_user')
    message = models.TextField()
    message_html = models.TextField(editable=False)
    created_at = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group,related_name='posts_group')

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering = ["created_at"]
        unique_together = ["user","message"]
