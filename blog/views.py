import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Post, Movies, Sliders, Advt
from django.contrib.auth.models import User


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class MoviesListView(ListView):
    model = Movies
    template_name = 'blog/home_movies.html'
    ordering = ['-date_released']
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super(MoviesListView, self).get_context_data(**kwargs)
        context.update({
            'sliders': Sliders.objects.all(),
            'move': Movies.objects.all(),
        })

        return context


class MoviesDetailListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = get_object_or_404(Movies, pk=self.kwargs.get('pk'))
        p = movie.name
        splitted = p.split()
        search = splitted[0]
        today = movie.date_released
        year = Movies.objects.filter(date_released__year=today.year)
        name = Movies.objects.filter(name__icontains=search)
        advt = Advt.objects.all()
        itemlist = name.union(year)
        context.update({
            'movie': movie,
            'move': Movies.objects.all(),
            'send': itemlist,
            'advt': advt,
        })
        return context

    def get_queryset(self):
        user = get_object_or_404(Movies, name=self.kwargs.get('name'))
        return Post.objects.filter(name=user).order_by('-date_posted')


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'  # app/model_viewtype.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    context_object_name = 'posts'
    fields = ['title', 'content', 'name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        return reverse("movies-detail", kwargs={'name': self.object.name, 'pk': self.object.name.pk})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/user_post_update.html'
    fields = ['title', 'content', 'name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        return reverse("movies-detail", kwargs={'name': self.object.name, 'pk': self.object.name.pk})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        return reverse("movies-detail", kwargs={'name': self.object.name, 'pk': self.object.name.pk})

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ComedyView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(comedy=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class ActionView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(action=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class SifiView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(sifi=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class ThrillerView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(thriller=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class AdventureView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(adventure=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class ClassicView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(classic=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class RomanceView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(Romance=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class AnimationView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(animation=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class DramaView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(drama=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class CrimeView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(crime=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class MysteryView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(mystery=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class FamilyView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(family=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class DocumentaryView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(documentary=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class FantasyView(ListView):
    template_name = "blog/geans.html"
    queryset = Movies.objects.filter(fantasy=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


def SearchView(request):
    search = request.GET['search']
    name = Movies.objects.filter(name__icontains=search)
    producer = Movies.objects.filter(by__icontains=search)
    date_released = Movies.objects.filter(date_released__icontains=search)
    itemlist = name.union(producer, date_released)
    context = {'movies': itemlist, 'search': search, 'move': Movies.objects.all()}

    return render(request, 'blog/search.html', context, )


class ComedyMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(comedy=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class ActionMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(action=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class SifiMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(sifi=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class ThrillerMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(thriller=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class AdventureMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(adventure=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class ClassicMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(classic=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class RomanceMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(Romance=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class AnimationMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(animation=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class DramaMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(drama=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class CrimeMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(crime=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class MysteryMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(mystery=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class FamilyMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(family=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class DocumentaryMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(documentary=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class FantasyMoviesView(ListView):
    template_name = "blog/geans_view.html"
    queryset = Movies.objects.filter(fantasy=True, series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class GeansMoviesView(ListView):
    template_name = "blog/geans_movies.html"
    queryset = Movies.objects.filter(series=False)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class ComedySeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(comedy=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class ActionSeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(action=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class SifiSeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(sifi=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class ThrillerSeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(thriller=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class AdventureSeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(adventure=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class ClassicSeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(classic=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class RomanceSeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(Romance=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class AnimationSeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(animation=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class DramaSeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(drama=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class CrimeSeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(crime=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class MysterySeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(mystery=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class FamilySeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(family=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class DocumentarySeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(documentary=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class FantasySeriesView(ListView):
    template_name = "blog/geans_view_series.html"
    queryset = Movies.objects.filter(fantasy=True, series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context


class GeansSeriesView(ListView):
    template_name = "blog/geans_series.html"
    queryset = Movies.objects.filter(series=True)
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'move': Movies.objects.all(),
        })
        return context
