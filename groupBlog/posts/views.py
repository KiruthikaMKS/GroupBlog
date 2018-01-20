from django.shortcuts import render
from django.views import generic as g
from braces.views import SelectRelatedMixin
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post
from groups.models import Group,GroupMember
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class ListPost(g.ListView,SelectRelatedMixin):
    model = Post
    select_related = ('user','group')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['user_groups'] = Group.objects.filter(members__in=[self.request.user])
        context['all_groups'] = Group.objects.all
        return context

class UserPost(g.ListView):
    model = Post
    # select_related = ('user','group')
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user=User.objects.prefetch_related('posts_user').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts_user.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class SinglePost(g.DetailView,SelectRelatedMixin):
    model = Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(g.CreateView,LoginRequiredMixin):
    model = Post
    fields = ('message','group')

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(g.DeleteView,SelectRelatedMixin,LoginRequiredMixin):
    model = Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)