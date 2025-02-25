from django import forms

from .models import Reviews, Rating, RatingStar


class ReviewForm(forms.ModelForm):
    """Пікір формасы"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")

class RatingForm(forms.ModelForm):
    """Рейтинг қосу формасы"""
    star= forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)
