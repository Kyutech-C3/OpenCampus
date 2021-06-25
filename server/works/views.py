from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from .forms import CommentForm
from django.utils import timezone

from .models import Work, Team, Genre, LiveSchedule

def genres(request):
    genres = Genre.objects.all()
    data_json = serializers.serialize('json', genres)
    print(data_json)

    # return render(request, 'works/index.html', context)
    return HttpResponse(data_json, content_type='application/json')

def work(request, work_id):
    work = Work.objects.get(pk=work_id)
    # comments = work.comment_set.all()
    # live_schedules = LiveSchedule.objects.all()
    data_json = serializers.serialize('json', work)
    return HttpResponse(data_json, content_type='application/json')

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
