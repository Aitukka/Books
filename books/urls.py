from  django.urls import path

from . import views


urlpatterns = [
    path("", views.BooksView.as_view(), name='book_list'),
    path("search/", views.Search.as_view(), name='search'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("<slug:slug>/", views.BookDetailView.as_view(), name="book_detail"),

    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),

]