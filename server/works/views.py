from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CommentForm
from django.utils import timezone

from .models import Work, Team, Genre, LiveSchedule

def index(request):
    genres = Genre.objects.all()
    live_schedules = LiveSchedule.objects.all()
    context = {
            "live_stream": isStreaming(live_schedules),
            "genres": genres,
        }

    return render(request, 'works/index.html', context)

def detail(request, work_id):
    work = Work.objects.get(pk=work_id)
    comments = work.comment_set.all()
    form = CommentForm()
    live_schedules = LiveSchedule.objects.all()
    context = {
        "work":work,
        "comments": comments,
        "form": form,
        "live_stream": isStreaming(live_schedules)
    }
    return render(request, 'works/detail.html', context)

def goods(request, work_id):
    work = Work.objects.get(pk=work_id)
    work.goods += 1
    work.save()
    return redirect(work)

def comment(request, work_id):
    work = Work.objects.get(pk=work_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.work = work
            comment.save()
    return redirect(work)

def isStreaming(schedules):
    res = None
    now = timezone.now()
    for schedule in schedules:
        if schedule.start <= now and schedule.end >= now:
            res =  schedule
    return res
