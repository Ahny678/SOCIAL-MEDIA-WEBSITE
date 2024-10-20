from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import VideoPost
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

@login_required
def base(request):
    return render(request, 'clone/base.html')

class PostVideoListView(View):
    def get(self, request, *args, **kwargs):
        my_videos = VideoPost.objects.filter(user=request.user)
        ordering = ['-post_date']

        context = {
         'my_videos' :my_videos
     }
        return render(request, 'clone/myvideos.html', context)
    
class PostVideoDetailView(DetailView):
    model = VideoPost

class PostVideoCreateView(LoginRequiredMixin,CreateView):
    model = VideoPost
    fields = ['video', 'thumbnail', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PostVideoUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = VideoPost
    fields = ['video', 'thumbnail', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class PostVideoDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = VideoPost
    success_url = '/base'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

