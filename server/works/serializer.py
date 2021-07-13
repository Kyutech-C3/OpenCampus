from typing import Iterable
from django.core import serializers
from django.db.models.base import Model
from rest_framework import serializers
from .models import Genre, Tag, Work, Comment
from datetime import datetime

class TagSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tag
		fields = ['id', 'name', 'color']

class WorkSerializer(serializers.ModelSerializer):
	# genre = GenreSerializer()

	class Meta:
		model = Work
		fields=['id', 'title', 'description', 'genre', 'team', 'thumbnail', 'goods', 'download_link', 'comments', 'tags', 'media_assets']
		depth = 1

class GenreSerializer(serializers.ModelSerializer):
	works = WorkSerializer(many=True)

	class Meta:
		model = Genre
		fields = ['id', 'works', 'title', 'description', 'bg_color']
		depth = 2


class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment
		fields=['id', 'name', 'text', 'work', 'created_at']
		depth = 1

	def create(self, validated_data):
		print('validated_data:', validated_data)
		print(self.initial_data)
		work = self.initial_data['work']
		return Comment.objects.create(**validated_data, work=work)