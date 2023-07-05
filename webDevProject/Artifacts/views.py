from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
         {'title': 'Обратная связь', 'url_name': 'contact'}]
def index(request):
    posts = Artifacts.objects.all()
    sets = Sets.objects.all()
    context = {'posts': posts,
               'sets': sets,
               'menu': menu,
               'title': 'Главная страница',
               'set_selected': 0}
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html', {'menu': menu, 'title': 'О сайте'})

def sets(request, setid):
    return HttpResponse(f"<h1>Артефакты по сетам</h1><p>{setid}</p>")

def contact(request):
    return HttpResponse("Обратная связь")

# def login(request):
#     return HttpResponse("Авторизация")


def logout_user(request):
    logout(request)
    return redirect('login')


def show_post(request, post_id):
    post = get_object_or_404(Artifacts, pk=post_id)
    set = get_object_or_404(Sets, pk=post.set_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'set_selected': post.set_id,
        'set': set
    }

    return render(request, 'post.html', context=context)

def show_set(request, set_id):
    posts = Artifacts.objects.filter(set_id=set_id)
    sets = Sets.objects.all()
    context = {'posts': posts,
               'sets': sets,
               'menu': menu,
               'title': 'Отображение по комплектам',
               'set_selected': set_id}
    return render(request, 'index.html', context=context)


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        sets = Sets.objects.all()
        context['menu'] = menu
        context['sets'] = sets
        if 'set_selected' not in context:
            context['set_selected'] = 0
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))



class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')