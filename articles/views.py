import markdown
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from django.http.response import JsonResponse

from articles.forms import ArticleForm, ColumnForm
from articles.models import Article, ArticleColumn


class IndexView(ListView):
    """
    首页视图
    """
    model = Article
    template_name = 'articles/index.html'
    context_object_name = 'articles'


class EditArticle(LoginRequiredMixin, View):
    """
    发布文章视图
    """

    def get(self, request):
        article_form = ArticleForm()
        columns = ArticleColumn.objects.filter(user=request.user)
        article_form.fields['column'].choices = [
            (column.id, column.name) for column in columns
        ]
        return render(request, 'articles/edit-article.html', {
            'article_form': article_form,
        })

    def post(self, request):
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            # 将文章内容转化为MarkDown格式
            article.content_html = markdown.markdown(
                article.content, extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc',
                ]
            )
            article.user = request.user
            article.save()
        return redirect('articles:index')


class ModifyArticleView(LoginRequiredMixin, View):
    """
    修改文章视图
    """
    pass


class ArticleDetailView(DetailView):
    """
    查看文章详情视图
    """

    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        return render(request, 'articles/article-detail.html', {
            'article': article
        })


class AddColumnView(LoginRequiredMixin, View):
    """
    栏目视图
    """

    def get(self, request):
        column_form = ColumnForm()
        return render(request, 'articles/add-column.html', {
            'column_form': column_form,
        })

    def post(self, request):
        column_form = ColumnForm(request.POST)
        if column_form.is_valid():
            column = column_form.save(commit=False)
            column.user = request.user
            column.save()
            return redirect('articles:index')
        else:
            return render(request, 'articles/add-column.html', {
                'column_form': column_form,
            })


@csrf_exempt
def upload_image(request):
    """
    文章上传图片视图
    """
    return JsonResponse({
        'status': 'ok'
    })