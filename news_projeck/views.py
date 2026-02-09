from django.shortcuts import render
from django.urls import reverse_lazy
from unicodedata import category

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ContactForm
from .models import News, Category
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

class CreateView(CreateView):
    model = News
    fields = ('title', 'slug', 'body', 'img', 'status')
    template_name = 'crud/create.html'
    success_url = reverse_lazy('news_list')


class EditView(UpdateView):
    model = News
    fields = ('title', 'slug', 'body', 'img', 'status')
    template_name = 'crud/news_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all()
        context['category'] = Category.objects.all()
        return context

class DeleteView(DeleteView):
    model = News
    template_name = 'crud/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by('-published_at')[:5]
        return context


def news_list(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all
    context = {
        'news': news
    }
    return render(request, 'list.html', context=context)

def news_detail(request, news):
    news_item = get_object_or_404(News, slug=news)
    print(f"Topilgan yangilik: {news_item.title}")
    context = {
        'new': news_item
    }
    return render(request, 'detail.html', context)


def home_page_view(request):
    categories = Category.objects.all()
    news = News.objects.filter(status=News.Status.Published)
    uzb_news = News.objects.filter(category__name='O‘zbekiston')[1:5]
    last_uzb_news = News.objects.filter(category__name='O‘zbekiston')[0]
    jahon_news = News.objects.filter(category__name='Jahon')
    iqtisodiyot_news = News.objects.filter(category__name='Iqtisodiyot')
    jamiyat_neews = News.objects.filter(category__name='Jamiyat')[1:5]
    last_jamiyat_news = News.objects.filter(category__name='Jamiyat')[0]
    texnologiya_news = News.objects.filter(category__name='Texnologiya')[1:5]
    last_texnologiya_news = News.objects.filter(category__name='Texnologiya')[0]
    rasmlar = News.objects.filter(status=News.Status.Published)[0:6]
    sport_news = News.objects.filter(category__name='Sport')[1:5]
    last_sport_news = News.objects.filter(category__name='Sport')[0]
    comentarya_news = News.objects.filter(status=News.Status.Published)[0:4]
    jahon_news_category = News.objects.filter(category__name='Jahon')[0:4]
    iqtisodiyot_news_category = News.objects.filter(category__name='Iqtisodiyot')[0:4]
    context = {
        'iqtisodiyot_news_category': iqtisodiyot_news_category,
        'jahon_news_category': jahon_news_category,
        'comentarya_news': comentarya_news,
        'sport_news': sport_news,
        'last_sport_news': last_sport_news,
        'rasmlar': rasmlar,
        'last_texnologiya_news': last_texnologiya_news,
        'texnologiya_news': texnologiya_news,
        'jamiyat_neews': jamiyat_neews,
        'last_jamiyat_news': last_jamiyat_news,
        'iqtisodiyot_news': iqtisodiyot_news,
        'jahon_news': jahon_news,
        'last_uzb_news': last_uzb_news,
        'uzb_news': uzb_news,
        'categories': categories,
        'news': news,
    }
    return render(request, 'home.html', context)


def contact_us(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("Xabaringiz yuborildi!")
    return render(request, 'contact.html', {"form": form})
    return render(request, 'contact.html', context)


def about_us(request):
    context = {}
    return render(request, 'about.html', context)


def page_404(request):
    context = {}
    return render(request, '404.html', context)
