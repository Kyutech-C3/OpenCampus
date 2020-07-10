from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Work, Team, Genre, LiveSchedule

def index(request):
    genres = Genre.objects.all()
    live_schedules = LiveSchedule.objects.all()
    context = {
            "isStreaming": isStreaming(live_schedules),
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

def isStreaming(schedules):
    res = False
    now = timezone.now()
    for schedule in schedules:
        if schedule.start <= now and schedule.end >= now:
            res =  True
    return res
