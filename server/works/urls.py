from django.urls import path

from . import views

urlpatterns = [
    path('genres', views.genres, name='genres'),
    path('works/<int:work_id>', views.work, name='works'),
    # path('<int:work_id>/goods', views.goods, name='work.goods'),
    # path('<int:work_id>/comment', views.comment, name='work.comment'),
]
