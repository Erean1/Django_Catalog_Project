from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView
from .models import Category,Film_Post,Comment
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from .forms import FilmPostForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
class Home(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
# def home(request):
#     category = Category.objects.all()
#     return render(request,'core/home.html',{'categories' : category})


class CategoryDetailPageView(DetailView):
    model = Category
    template_name = 'core/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object
        context['films'] = category.film_post_set.all()
        return context

# def category_detail_view(request,slug):
#     category = get_object_or_404(Category,slug=slug)
#     films = category.film_post_set.all()

#     return render(request,'core/category_detail.html',{'category' : category,'films' : films})


class CreatePostView(LoginRequiredMixin,CreateView):
    model = Film_Post
    form_class = FilmPostForm
    template_name = 'core/create_post.html'
    login_url = 'users:login'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self,**kwargs):
        return reverse('core:post_detail',kwargs={'slug' : self.object.slug})

# def create_post_view(request):
#     if request.method == "POST":
#         form = FilmPostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
            
#     else:
#         form = FilmPostForm()
    
#     return render(request,'core/create_post.html',{'form' : form,'categories' : Category.objects.all()})



class PostDetailView(DetailView):
    model = Film_Post
    template_name = 'core/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        return context


    
# def post_detail_view(request,slug):
#     post = get_object_or_404(Film_Post,slug=slug)
#     return render(request,'core/post_detail.html',{'post' : post})



class PostEditView(LoginRequiredMixin,UpdateView):
    model = Film_Post
    template_name = "core/post_edit.html"
    fields = ['description','category','title','image','director']
    success_url = reverse_lazy('core:home')
    
    def get_success_url(self,**kwargs):

        return reverse('core:post_detail',kwargs={'slug' : self.object.slug})
    
# def post_edit_view(request, slug):
#     post = get_object_or_404(Film_Post, slug=slug)
    
#     if request.method == 'POST':
#         form = FilmPostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('core:post_detail', slug=post.slug)
#     else:
#         form = FilmPostForm(instance=post)

#     return render(request, 'core/post_edit.html', {'form': form, 'post': post})


class PostDeleteView(DeleteView):
    model = Film_Post
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy("core:home")

# def post_delete_view(request, slug):
#     post = get_object_or_404(Film_Post, slug=slug)
    
#     if request.method == 'POST':
#         post.delete()
#         return redirect('core:home')
    
#     return render(request, 'core/confirm_delete.html', {'post': post})

class AddCommentView(LoginRequiredMixin,CreateView):
    model = Comment
    login_url = 'users:login'
    form_class = CommentForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Film_Post,slug=self.kwargs['slug'])
        return super().form_valid(form)
    
    def get_success_url(self,**kwargs):
        return reverse_lazy('core:post_detail',kwargs={'slug' : self.object.post.slug})


