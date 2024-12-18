from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.views import generic
from . import models

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    paginate_by = 5

    def get_queryset(self):
        return models.books.objects.filter(title__icontains=self.request.GET.get('q')).order_by('id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



def books_list(request):
    if request.method == "GET":
        book_list = models.books.objects.filter().order_by("-id")
        context = {"book_list": book_list}
        return render(request, template_name="book.html", context=context)


def books_detail(request, id):
    if request.method == "GET":
        book_id = get_object_or_404(models.books, id=id)
        context = {"book_id": book_id}
        return render(request, template_name="book_detail.html", context=context)


def about_me(request):
    if request.method == "GET":
        return HttpResponse("My name is Daniel Abdykadyrov")


def about_pets(request):
    if request.method == "GET":
        return HttpResponse("I dont have any pets in my home!")


def show_time(request):
    if request.method == "GET":
        return HttpResponse(datetime.now())
