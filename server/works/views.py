from django.http import HttpResponse
from django.shortcuts import render
from .models import Work, Team


def index(request):
    context = {
            "unity3d": Work.objects.filter(type_choice=Work.WorkType.UNITY_3D),
            "unity2d": Work.objects.filter(type_choice=Work.WorkType.UNITY_2D),
            "video": Work.objects.filter(type_choice=Work.WorkType.VIDEO),
            "model3d": Work.objects.filter(type_choice=Work.WorkType.MODEL_3D),
            "other": Work.objects.filter(type_choice=Work.WorkType.OTHER)
        }

    return render(request, 'works/index.html', context)

def detail(request, work_id):
    work = Work.objects.get(pk=work_id)
    team = work.team
    context = {
        "work":work
    }
    return render(request, 'works/detail.html', context)
