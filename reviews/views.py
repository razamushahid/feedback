from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

# Create your views here.
from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "user_form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect("thank-you")


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


def thank_you(request):
    return render(request, "reviews/thank_u.html")
