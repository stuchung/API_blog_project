"""posts URL Configuration"""

from django.urls import path, include

""" this was the origial import from post/views when there were four """
# from .views import PostDetail, PostList, UserList, UserDetail

""" The new imports to use viewsets """
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet


""" this was the old routing patter for the four origial views """
# urlpatterns = [
#     path('users', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('', PostList.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
# ]

""" The new URL patter to config viewsets """

router = SimpleRouter()
router.register('users', UserViewSet, base_name ='users')
router.register('', PostViewSet, base_name ='posts')

urlpatterns = router.urls
