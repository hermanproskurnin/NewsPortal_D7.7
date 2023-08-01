from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.


class PostsList(ListView):

    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, по которому будем сортировать (указываем, что сортировка будет по убыванию создания)
    ordering = "-date_of_post"
    # Указываем имя шаблона, в котором будут содержаться все инструкции
    template_name = "news.html"
    # Имя списка, в котором лежат все наши новости, нужно для обращения в html-шаблоне
    context_object_name = "posts"
    
    # Post.objects.all()
    # Добавляем пагинацию, 10 новостей на страницу
    paginate_by = 10

    # # Переопределяем функцию получения списка новостей
    # def get_queryset(self):
    #     # Обычный запрос
    #     queryset = super().get_queryset()
    #     # Используем наш класс фильтрации.
    #     # self.request.GET содержит объект QueryDict.
    #     # Сохраняем нашу фильтрацию в объекте класса,
    #     # чтобы потом добавить в контекст и использовать в шаблоне.
    #     self.filterset = PostFilter(self.request.GET, queryset=queryset)
    #     # Возвращаем отфильтрованный список новостей
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Добавляем в контекст объект фильтрации.
    #     context['search_filter'] = self.filterset
    #     return context


class PostDetail(DetailView):

    # Модель используем ту же
    model = Post
    # Шаблон будет другим
    template_name = "new.html"
    # Название объекта, в котором будет выбранная новость
    context_object_name = "post"

    # Этот метод позволяет изменять набор данных, передающихся в шаблон
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context["time_now"] = datetime.utcnow()

        return context


# Поиск статей
class PostSearch(ListView):
    model = Post
    ordering = '-date_of_post'
    template_name = 'post_search.html'
    context_object_name = 'posts_search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# Добавляем новое представление для создания статей.
class NewsCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель статей
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'create_post.html'
    # возвращаемся после создания на страницу с новостями
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Создать новость'
        return context


class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create_post.html'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Создать статью'
        return context


# Представление для изменения новости одинаково с созданием, используем только другой дженерик
class NewsEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'create_post.html'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Редактировать новость'
        return context


class ArticleEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'create_post.html'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Редактировать статью'
        return context


class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Удалить новость'
        context['previous_page_url'] = reverse_lazy('post_list')
        return context


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Удалить статью'
        context['previous_page_url'] = reverse_lazy('post_list')
        return context
