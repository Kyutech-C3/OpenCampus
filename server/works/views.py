from copy import copy
from django.core.exceptions import ValidationError
from django.db.models import query
from django.http.response import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect
from .serializer import CommentSerializer, GenreSerializer, WorkSerializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from .forms import CommentForm
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
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

class PostGoodsViewSet(viewsets.GenericViewSet, CreateModelMixin):
    serializer_class = WorkSerializer

    def create(self, request, *args, **kwargs):
        print(kwargs)
        work = Work.objects.get(pk=kwargs['work_pk'])
        if work == None:
            return Response(data='Specified work does not exist', status=status.HTTP_404_NOT_FOUND)

        work.goods += 1
        work.save()

        serializer = WorkSerializer(instance=work)
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DownloadRedirectViewSet(viewsets.GenericViewSet):

    def list(self, request, *args, **kwargs):
        work = Work.objects.get(pk=kwargs['work_pk'])
        url = work.download_link
        if url == None:
            return HttpResponseNotFound()
        work.downloaded_count += 1
        work.save()
        return HttpResponseRedirect(url)