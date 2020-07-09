from django.http import HttpResponse
from django.shortcuts import render

from .models import Work, Team, Genre

def index(request):
    genres = Genre.objects.all()
    context = {
            "genres": genres,
        }

    return render(request, 'works/index.html', context)

def detail(request, work_id):
    work = Work.objects.get(pk=work_id)
    team = work.team
    context = {
        "work":work
    }
    return render(request, 'works/detail.html', context)
