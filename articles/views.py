from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ('title','body',)

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list.html")
class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ('title','body','author',)


# Create your views here.
