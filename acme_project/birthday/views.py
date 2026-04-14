from django.shortcuts import render, get_object_or_404, redirect
from .forms import BirthdayForm
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown
from .models import Birthday
# Импортируем класс пагинатора.
from django.core.paginator import Paginator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

# Создаём миксин.
class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')

class BirthdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


# Добавляем миксин первым по списку родительских классов.
class BirthdayCreateView(BirthdayMixin, BirthdayFormMixin, CreateView):
    # Не нужно описывать атрибуты: все они унаследованы от BirthdayMixin.
    pass


class BirthdayUpdateView(BirthdayMixin, BirthdayFormMixin, UpdateView):
    # И здесь все атрибуты наследуются от BirthdayMixin.
    pass 


# Наследуем класс от встроенного ListView:
class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 10 


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list') 