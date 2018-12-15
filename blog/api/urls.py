from django.conf.urls import url, include
from rest_framework import routers
from blog.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    url(r'^(?P<pk>\d+)/$', views.PostListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/edit/$', views.PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.PostDeleteAPIView.as_view(), name='delete'),
]

