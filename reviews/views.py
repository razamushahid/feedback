from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
# Create your views here.
from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "thank-you"

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "thank-you"
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


    # def get(self, request):
    #     form = ReviewForm()
    #
    #     return render(request, "reviews/review.html", {
    #         "user_form": form
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         form.save()
    #         return HttpResponseRedirect("thank-you")


def review(request):
    # print(request.__dict__)
    # if request.method == 'POST':
    #     print(request.POST['username'])
    #     entered_username = request.POST['username']
    #     if entered_username == "":
    #         return render(request, "reviews/review.html", {
    #             "has_error": True
    #         })
    #     return HttpResponseRedirect("thank-you")
    # # Other than POST request
    # return render(request, "reviews/review.html", {
    #     "has_error": False
    # })
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # user_review = Review(username=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'],
            #                      rating=form.cleaned_data['rating'])
            # user_review.save()
            form.save()
            return HttpResponseRedirect("thank-you")
    else:
        form = ReviewForm()
    return render(request, "reviews/review.html", {
        "user_form": form
    })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_u.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Well,This works!"
        return context


    # def get(self, request):
    #     print(self.__class__)
    #     return render(request, "reviews/thank_u.html")

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gte=1)
        return data


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context['reviews'] = reviews
    #     return context


class ReviewDetailView(DetailView):
    template_name = "reviews/single_review_detail.html"
    model = Review


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     single_review = get_object_or_404(Review, pk=kwargs['id'])
    #     context['review'] = single_review
    #     return context


def thank_you(request):
    return render(request, "reviews/thank_u.html")
