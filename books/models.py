from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    """Кітаптар"""
    title = models.CharField("Аты", max_length=100)
    description = models.TextField("Сипаттамасы")
    poster = models.ImageField("Кітап", upload_to="books/")
    year = models.PositiveSmallIntegerField("Шыққан жылы", default=2010)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    book_file = models.FileField("Файл кітап", upload_to="book_files/", null=True, blank=True)


    def get_absolute_url(self):
        return reverse('book_detail', kwargs={"slug": self.url})
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кітап"
        verbose_name_plural = "Кітаптар"

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

class RatingStar(models.Model):
    """Баға беру жұлдыздары"""
    value = models.PositiveSmallIntegerField("Мәні", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Баға беру жұлдызы"
        verbose_name_plural = "Баға беру жұлдыздары"
        ordering = ["-value"]


class Rating(models.Model):
    """Баға беру жұлдыздары"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="жұлдыз")
    book= models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="кітап")

    def __str__(self):
        return f"{self.star}={self.book}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтингтер"

class Reviews(models.Model):
    """Пікірлер"""
    email = models.EmailField()
    name = models.CharField("Аты", max_length=100)
    text= models.TextField("Текст", max_length=5000)
    parent= models.ForeignKey(
       'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
       )
    book = models.ForeignKey(Book, verbose_name="кітап", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}={self.book}"

    class Meta:
        verbose_name = "Пікір"
        verbose_name_plural = "Пікірлер"