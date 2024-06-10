from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View


from .models import Book, Rating
from .forms import  ReviewForm, RatingForm
# Create your views here.

class BooksView(ListView):
    """Кітаптар тізімі"""
    model = Book
    queryset = Book.objects.filter(draft=False)
    paginate_by = 2


class BookDetailView(DetailView):
    """Кітап сипаттамасы"""
    model = Book
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context


class AddReview(View):
    """Пікірлер"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            review = form.save(commit=False)
            review.book = book
            review.save()
        return redirect(book.get_absolute_url())

class Search(ListView):
    """Поиск фильмов"""
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                book_id=int(request.POST.get("book")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)



def book_detail(request, book_id):
        # Получаем все оценки для книги
        ratings = Rating.objects.filter(book_id=book_id)

        # Рассчитываем среднее значение всех оценок
        if ratings.exists():
            average_rating = sum(rating.star for rating in ratings) / len(ratings)
        else:
            average_rating = 0.0

        context = {
            'ratings': ratings,
            'average_rating': average_rating,
        }
        return render(request, 'book_detail.html', context)