from django.http import HttpResponse
from django.shortcuts import render
from .models import Work, Team


def index(request):
    return HttpResponse("Hello, you can see works.")

def detail(request, work_id):
    work = Work.objects.get(pk=work_id)
    team = work.team
    context = {
        "work":work
    }
    return render(request, 'works/detail.html', context)