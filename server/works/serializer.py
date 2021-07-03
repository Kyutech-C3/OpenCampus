from typing import Iterable
from django.core import serializers
from django.db.models.base import Model
from rest_framework import serializers
from .models import Genre, Work, Comment
from datetime import datetime

class GenreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Genre
		fields = ['id', 'works', 'title', 'bg_color']
		depth = 2

class WorkSerializer(serializers.ModelSerializer):
	# genre = GenreSerializer()

	class Meta:
		model = Work
		fields=['id', 'title', 'description', 'genre', 'team', 'type_choice', 'goods', 'comments']
		depth = 1

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