from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from groups.models import Group,GroupMember
from django.db import IntegrityError
from django.contrib import messages
# Create your views here.
from django.views import generic as g

class CreateGroup(g.CreateView,LoginRequiredMixin):
    model = Group
    fields = ('name','description')

class SingleGroup(g.DetailView):
    model = Group

class ListGroup(g.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin,g.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,'already a member')
        else:
            messages.success(self.request,'join success')
        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,g.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            membership = GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug'))
        except GroupMember.DoesNotExist:
            messages.warning(self.request,*args,**kwargs)
        else:
            membership.delete()
            messages.success(self.request,'left success')
        return super().get(request,*args,**kwargs)

    
