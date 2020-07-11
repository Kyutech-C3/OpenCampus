from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='works'),
    path('<int:work_id>/', views.detail, name='work'),
    path('<int:work_id>/goods', views.goods, name='work.goods'),
    path('<int:work_id>/comment', views.comment, name='work.comment'),
]
