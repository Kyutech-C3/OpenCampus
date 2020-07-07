from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Work, Team, Comment
from .forms import CommentPostForm

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
    comments = Comment.objects.filter(work=work)

    # Receive Comment Post
    if request.method == 'POST':
        form = CommentPostForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.work = work
            comment.save()
            
            return redirect(comment)
    
    form = CommentPostForm()
    context = {
        "work":work,
        "comments": comments,
        "form": form,
    }
    return render(request, 'works/detail.html', context)
