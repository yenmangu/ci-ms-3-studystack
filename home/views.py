from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:

    context = {
        "page_title": "StudyStack | Home",
        "page_description": "Community-driven study resources shared by learners",
        "page_keywords": "study resources, education, learning, StudyStack",
    }

    return render(request, "home/home.html", context)
