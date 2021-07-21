from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register(r'genres', views.GenreViewSet)
router.register(r'works', views.WorkViewSet)

works_router = routers.NestedDefaultRouter(router, r'works', lookup='work')
works_router.register(r'comments', views.CommentViewSet, basename='work-comments')
works_router.register(r'goods', views.PostGoodsViewSet, basename='work-goods')
works_router.register(r'download', views.DownloadRedirectViewSet, basename='work-download')


urlpatterns = (
    url(r'^', include(router.urls)),
    url(r'^', include(works_router.urls)),
    # path(r'works/{pk}/goods/', views.PostGoods.as_view())
    # path(r'works/{work_pk}/goods', views.post_work_goods)
)