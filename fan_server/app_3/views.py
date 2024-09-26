from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from .filters import ResponseFilter
from .models import Post, Response, User
from .forms import PostForm, ResponseForm


class PostList(ListView):
    model = Post
    ordering = 'author'
    template_name = 'post.html'
    context_object_name = 'post'


class PersonalPost(ListView):
    model = Post
    template_name = 'post_personal.html'
    context_object_name = 'personal_post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)



class IdPostList(DetailView):
    model = Post
    template_name = 'post_id.html'
    context_object_name = 'post_id'


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = '/post/'


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    success_url = '/post/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class ResponseList(LoginRequiredMixin, ListView):
    form_class = ResponseForm
    model = Response
    template_name = 'response.html'
    context_object_name = 'response'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset().filter(post__author=self.request.user)
        self.filterset = ResponseFilter(self.request.GET, queryset, request=self.request.user.id)
        return self.filterset.qs


class ResponseCreate(LoginRequiredMixin, CreateView):
    form_class = ResponseForm
    model = Response
    template_name = 'response_create.html'
    success_url = '/post/'

    def form_valid(self, form):
        response = form.save(commit=False)
        response.author = self.request.user
        response.save()
        return super().form_valid(form)


class ResponseDelete(DeleteView):
    model = Response
    template_name = 'response_delete.html'
    success_url = '/response/'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/post/personal/'

def response_status_update(request, pk):
    resp = Response.objects.get(pk=pk)
    resp.status = True
    resp.save()
    return redirect(reverse_lazy('response'))


class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'users/invalid_code.html')
            return redirect('account_login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'post.html'
