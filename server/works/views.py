from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Work, Team, Genre

def index(request):
    genres = Genre.objects.all()
    context = {
            "genres": genres,
        }

    return render(request, 'works/index.html', context)

def detail(request, work_id):
    work = Work.objects.get(pk=work_id)
    context = {
        "work":work,
    }
    return render(request, 'works/detail.html', context)

def goods(request, work_id):
    work = Work.objects.get(pk=work_id)
    work.goods += 1
    work.save()
    return redirect(work)
