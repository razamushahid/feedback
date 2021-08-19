from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView

from .forms import ProfileForm


# Create your views here.
from .models import UserProfile


# def store_file(file):
#     try:
#         with open("temp/image.jpg", "wb+") as f:
#             for chunk in file.chunks():
#                 f.write(chunk)
#     except Exception:
#         print(f"File already Exist: {f.name}")


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    # form_class = ProfileForm
    fields = "__all__"
    success_url = "/profiles"


# class CreateProfileView(View):
#
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })
#
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         print("Post: Submitted Form")
#         if submitted_form.is_valid():
#             file = request.FILES['user_image']
#             profile = UserProfile(image=file)
#             profile.save()
#             # store_file(file)
#             return HttpResponseRedirect("/profiles")
#
#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })


class ProfileViews(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"





