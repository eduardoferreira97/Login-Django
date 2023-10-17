from django.shortcuts import render


def home(request):
    return render(request, "global/index.html", context={"name": "Eduardo José"})
