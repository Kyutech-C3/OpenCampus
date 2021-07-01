from copy import copy
from django.core.exceptions import ValidationError
from django.db.models import query
from django.http.response import HttpResponseBadRequest
from .serializer import CommentSerializer, GenreSerializer, WorkSerializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from .forms import CommentForm
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics, viewsets
import io

from .models import Work, Genre, Comment


class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        print('kwargs', self.kwargs)
        return Comment.objects.filter(work=self.kwargs['work_pk'])
   
    def create(self, request, work_pk=None):
        work = generics.get_object_or_404(Work.objects, pk=work_pk)
        temp_data = {
            'name': request.data.get('name'),
            'text': request.data.get('text'),
            'work': work
        }
        request._full_data = temp_data
        print(request.data)
        return super(CommentViewSet, self).create(request)
