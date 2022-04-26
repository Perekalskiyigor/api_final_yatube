from django.urls import path, include
# urls.py
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
from rest_framework.authtoken import views

router_v1 = SimpleRouter() 
router_v1.register('posts', PostViewSet, basename='api/v1/posts')
router_v1.register('groups', GroupViewSet, basename='api/v1/groups')
router_v1.register(r'posts/(?P<post_id>[^/.]+)/comments',
                   CommentViewSet, basename='api/v1/comments')
router_v1.register('follow', FollowViewSet, basename='following')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('v1/api-token-auth/', views.obtain_auth_token),
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('v1/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),

]
