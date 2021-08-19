from django.urls import path

from . import views

urlpatterns = [
    # path('', views.review),
    # path('thank-you', views.thank_you)
    path('', views.ReviewView.as_view()),
    path('thank-you', views.ThankYouView.as_view()),
    path('review-list', views.ReviewListView.as_view()),
    path('favorite', views.AddFavoriteView.as_view()),
    path('review-detail/<int:pk>', views.ReviewDetailView.as_view(), name="review-detail"),
    # path('thank-you', views.thank_you)
]